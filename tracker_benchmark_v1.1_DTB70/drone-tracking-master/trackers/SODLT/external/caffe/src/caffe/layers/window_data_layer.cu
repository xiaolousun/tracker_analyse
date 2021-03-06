//
// Based on data_layer.cpp by Yangqing Jia.

#include <pthread.h>
#include <stdint.h>

#include <string>
#include <vector>

#include "caffe/layer.hpp"
#include "caffe/util/io.hpp"
#include "caffe/vision_layers.hpp"
#include "caffe/data_layers.hpp"
// caffe.proto > LayerParameter > WindowDataParameter
//   'source' field specifies the window_file
//   'crop_size' indicates the desired warped size

namespace caffe {

template <typename Dtype>
void WindowDataLayer<Dtype>::Forward_gpu(const vector<Blob<Dtype>*>& bottom,
      vector<Blob<Dtype>*>* top) {
  // First, join the thread
  JoinPrefetchThread();
  // Copy the data
  caffe_copy(prefetch_data_.count(), prefetch_data_.cpu_data(),
      (*top)[0]->mutable_gpu_data());
  caffe_copy(prefetch_label_.count(), prefetch_label_.cpu_data(),
      (*top)[1]->mutable_gpu_data());
  if (top->size() > 2){
    caffe_copy(prefetch_box_.count(), prefetch_box_.cpu_data(),
             (*top)[2]->mutable_gpu_data());
  }
  // Start a new prefetch thread
  CreatePrefetchThread();
}

template <typename Dtype>
Dtype WindowDataLayer<Dtype>::Backward_gpu(const vector<Blob<Dtype>*>& top,
      const bool propagate_down, vector<Blob<Dtype>*>* bottom) {
  return Dtype(0.);
}

INSTANTIATE_CLASS(WindowDataLayer);

}  // namespace caffe
