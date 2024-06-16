import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split


def load_data(path):
    images = []
    labels = []
    label_to_index = {}
    index = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                file_path = os.path.join(root, file)
                label = os.path.basename(root)
                if label not in label_to_index:
                    label_to_index[label] = index
                    index += 1
                image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                if image is None:
                    print(f"Can't load: {file_path}")
                    continue
                image = cv2.resize(image, (28, 28))
                images.append(image)
                labels.append(label)

    labels = np.array([label_to_index[label] for label in labels])
    return np.array(images), labels


data_directory = r"D:\Dataset\Cards"

images, labels = load_data(data_directory)

images = images.reshape(-1, 28, 28, 1).astype('float32') / 255.0
labels = to_categorical(labels, num_classes=len(np.unique(labels)))

train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

print(f'train_images: {train_images.shape}')
print(f'train_labels: {train_labels.shape}')
print(f'test_images: {test_images.shape}')
print(f'test_labels: {test_labels.shape}')


def create_model(num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)),
        Conv2D(32, (3, 3), padding='same', activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        Conv2D(64, (3, 3), padding='same', activation='relu'),
        Conv2D(64, (3, 3), padding='same', activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


num_classes = len(np.unique(np.argmax(train_labels, axis=1)))

model = create_model(num_classes=num_classes)
model.fit(train_images, train_labels, batch_size=128, epochs=10, validation_data=(test_images, test_labels))

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Accuracy: {test_accuracy}')

model.save('PokerMan.h5')
