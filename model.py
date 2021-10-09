import tensorflow as tf

LAYERS = [
          tf.keras.layers.Flatten(input_shape = [28,28], name = "InputLayer"),
          tf.keras.layers.Dense(300, activation="relu",name="hiddenLayer1"),
          tf.keras.layers.Dense(100, activation="relu",name="hiddenLayer2"),
          tf.keras.layers.Dense(10, activation="softmax",name="outputLayer")
]

model_clf = tf.keras.models.Sequential(LAYERS)

LOSS_FUNCTION = "sparse_categorical_crossentropy"
OPTIMIZER = "SGD"
METRICS = ['accuracy']

model_clf.compile(loss=LOSS_FUNCTION, optimizer=OPTIMIZER, metrics=METRICS)

X_valid, X_train = X_train_full[:5000]/255., X_train_full[:55000]/255.
y_valid, y_train = y_train_full[:5000], y_train_full[:55000]
X_test = X_test/255

EPOCHS = 30
VALIDATION = (X_valid, y_valid)

history = model_clf.fit(X_train, y_train, epochs=EPOCHS, validation_data=VALIDATION)