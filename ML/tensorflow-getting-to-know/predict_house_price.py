import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32, [None, 1])
W = tf.Variable(tf.zeros([1, 1]))
b = tf.Variable(tf.zeros([1]))

y = tf.matmul(x, W) + b  # linear model
y_ = tf.placeholder(tf.float32, [None, 1])
cost = tf.reduce_sum(tf.pow((y_ - y), 2))

# generate inputs
for i in xrange(100):
    # create fake data for actual data
    xs = np.array([[i]])
    ys = np.array([[2 * i]])


train_step = tf.train.GradientDescentOptimizer(0.00001).minimize(cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
steps = 400
for i in xrange(steps):
    xs = np.array([[i]])
    ys = np.array([[2 * i]])

    # train
    feed = {x: xs, y_: ys}
    sess.run(train_step, feed_dict = feed)

    print "After %d iteration, W: %f, b: %f, cost: %f" % (i, sess.run(W), sess.run(b))
