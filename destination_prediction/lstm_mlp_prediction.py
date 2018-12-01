import torch
from torch import nn
import numpy as np
import torch.utils.data as Data
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
EPOCH = 10  # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 64
TIME_STEP = 10  # rnn time step / image height
INPUT_SIZE = 30  # rnn input size / image width
HIDDEN_SIZE = 128
LR = 0.01  # learning rate

labels = list(np.load("F:\FCD data\cluster\destination_labels.npy"))
# label个数
label_size = len(set(labels))


def load_data():
    filepath = "F:\FCD data\\trajectory\workday_trajectory_destination\youke_1_result_npy.npy"
    trajectories = list(np.load(filepath))
    count = len(trajectories) * 0.8

    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    car_to_ix = {}
    poi_to_ix = {}
    region_to_ix = {}
    for trajectory, label in trajectories:
        for t in trajectory:
            if t[0] not in car_to_ix:
                car_to_ix[t[0]] = len(car_to_ix)
            if t[-1] not in poi_to_ix:
                poi_to_ix[t[-1]] = len(poi_to_ix)
            if t[-2] not in region_to_ix:
                region_to_ix[t[-2]] = len(region_to_ix)

    def transfer(tra):
        new_tra = []
        for t in tra:
            new_t = []
            new_t.append(car_to_ix[t[0]])
            new_t.append(region_to_ix[t[5]])
            new_t.append(poi_to_ix[t[6]])
            new_tra.append(new_t)
        return new_tra

    # 过滤轨迹，如果轨迹存在连续相同区域，则进行过滤
    def filter(tra):
        first_index = tra[0]
        new_tra = [tra[0]]
        for t in tra:
            if t[1] == first_index[1]:
                continue
            new_tra.append(t)
            first_index = t
        return new_tra

    c = 0
    for trajectory, label in trajectories:
        new_tra = transfer(trajectory)
        new_tra = filter(new_tra)
        if len(new_tra) < 10:
            c += 1
            continue
        if c < count:
            train_data.append(new_tra[:5] + new_tra[-5:])
            train_labels.append(label)
        else:
            test_data.append(new_tra[:5] + new_tra[-5:])
            test_labels.append(label)
        c += 1
    return train_data, train_labels, test_data, test_labels, car_to_ix, poi_to_ix


train_data, train_labels, test_data, test_labels, car_to_ix, poi_to_ix = load_data()
train_data = torch.FloatTensor(train_data)
train_labels = torch.LongTensor(train_labels)
test_data = torch.FloatTensor(test_data)
test_labels = torch.LongTensor(test_labels).numpy()

torch_dataset = Data.TensorDataset(train_data, train_labels)
loader = Data.DataLoader(
    dataset=torch_dataset,  # torch TensorDataset format
    batch_size=BATCH_SIZE,  # mini batch size
    shuffle=True  # 要不要打乱数据 (打乱比较好)
)


class EncoderRNN(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(EncoderRNN, self).__init__()
        self.hidden_size = hidden_size

        self.lstm = nn.LSTM(
            input_size=INPUT_SIZE,
            hidden_size=128,  # rnn hidden unit
            num_layers=2,  # number of rnn layer
            batch_first=True,  # input & output will has batch size as 1s dimension. e.g. (batch, time_step, input_size)
        )
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.car_embeds = nn.Embedding(len(car_to_ix), 10)
        self.poi_embeds = nn.Embedding(len(poi_to_ix), 10)
        self.region_embeds = nn.Embedding(1067, 10)

    def forward(self, x, hidden):
        new_vector = None
        for vector in x:
            for item in vector:
                if new_vector is None:
                    new_vector = torch.cat((self.car_embeds(torch.LongTensor([item[0].item()]))[0],
                                            self.region_embeds(torch.LongTensor([item[1].item()]))[0]))
                    new_vector = torch.cat((new_vector, self.poi_embeds(torch.LongTensor([item[2].item()]))[0]))
                else:
                    new_vector = torch.cat((new_vector, self.car_embeds(torch.LongTensor([item[0].item()]))[0]))
                    new_vector = torch.cat((new_vector, self.region_embeds(torch.LongTensor([item[1].item()]))[0]))
                    new_vector = torch.cat((new_vector, self.poi_embeds(torch.LongTensor([item[2].item()]))[0]))
        x = new_vector.view(-1, 10, 30)

        embedded = self.embedding(input).view(1, 1, -1)
        output = embedded
        output, hidden = self.lstm(output, hidden)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size, device=device)


class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(784, 100),
            nn.ReLU(),
            nn.Linear(100, 10)
        )

    def forward(self, x):
        # convert tensor (128, 1, 28, 28) --> (128, 1*28*28)
        x = x.view(x.size(0), -1)
        x = self.layers(x)
        return x


encoder = EncoderRNN(INPUT_SIZE, HIDDEN_SIZE)
print(encoder)
mlp = MLP()
print(mlp)


# 对轨迹序列进行循环训练，得到最后时刻的隐藏状态
def train(b_x):
    encoder_hidden = encoder.initHidden()

    for vector in b_x:
        for item in vector:
            encoder_output, encoder_hidden = encoder(item, encoder_hidden)

    mlp_output = mlp(encoder_hidden)
    return mlp_output


encoder_optimizer = torch.optim.Adam(encoder.parameters(), lr=LR)
mlp_optimizer = torch.optim.Adam(mlp.parameters(), lr=LR)

loss_func = nn.CrossEntropyLoss()  # the target label is not one-hotted

# training and testing
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(loader):  # gives batch data
        b_x = b_x.view(-1, 10, 3)  # reshape x to (batch, time_step, input_size)

        output = train(b_x)
        loss = loss_func(output, b_y)  # cross entropy loss
        encoder_optimizer.zero_grad()  # clear gradients for this training step
        mlp_optimizer.zero_grad()
        loss.backward()  # backpropagation, compute gradients
        encoder_optimizer.step()  # apply gradients
        mlp_optimizer.step()

        if step % 50 == 0:
            test_output = train(test_data)  # (samples, time_step, input_size)
            pred_y = torch.max(test_output, 1)[1].data.numpy()
            accuracy = float((pred_y == test_labels).astype(int).sum()) / float(test_labels.size)
            print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)

# print 10 predictions from test data
test_output = train(test_data[:10].view(-1, 10, 3))
pred_y = torch.max(test_output, 1)[1].data.numpy()
print(pred_y, 'prediction number')
print(test_labels[:10], 'real number')
