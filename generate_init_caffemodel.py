#Rosun
#python script
# The caffe module needs to be on the Python path;
import sys
caffe_root = '../../'  # this file should be run from {caffe_root}/examples (otherwise change this line)
sys.path.insert(0, caffe_root + 'python')  #pycaffe dir
import caffe

def show_network_configuration(proto_file,caffemodel_file):
    # Load the original network and extract the network  layers' parameters.
    net = caffe.Net(proto_file, caffemodel_file, caffe.TEST)  
    
    #look at the parameter shapes. The parameters are exposed as another OrderedDict, net.params. 
    #We need to index the resulting values with either [0] for weights or [1] for biases.
    for layer_name, param in net.params.iteritems():
        print layer_name + '\t' + str(param[0].data.shape)
    # for each layer, show the output shape
    for layer_name, blob in net.blobs.iteritems():
        print layer_name + '\t' + str(blob.data.shape)

prototxt_file='pspnet101_VOC2012_473_val.prototxt'
caffemodel_file='../model/pspnet101_VOC2012.caffemodel'
show_network_configuration(prototxt_file,caffemodel_file)
