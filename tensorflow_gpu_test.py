import tensorflow as tf

print(tf.__version__)
# tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
