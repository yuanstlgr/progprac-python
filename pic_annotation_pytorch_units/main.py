import torch
import os
from torchvision import datasets, transforms

# Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,))])

# Load the training data
folder_path = os.path.join(os.path.dirname(__file__), 'pytorch_train_folder')
train_data = datasets.ImageFolder(folder_path, transform=transform)

# Create a data loader
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)


from torch import nn, optim

# Define the model
model = nn.Sequential(nn.Linear(784, 256),
                      nn.ReLU(),
                      nn.Linear(256, 10),
                      nn.LogSoftmax(dim=1))

# Define the loss
criterion = nn.NLLLoss()

# Define the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.003)

# Train the model
epochs = 5
for e in range(epochs):
    running_loss = 0
    for images, labels in train_loader:
        # Flatten images into a 784 long vector
        images = images.view(images.shape[0], -1)

        # Training pass
        optimizer.zero_grad()

        output = model(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    else:
        print(f"Training loss: {running_loss / len(train_loader)}")