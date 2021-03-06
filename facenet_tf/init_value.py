import os
import facenet_tf.src.common.download_and_extract as download_and_extract
import facenet_tf.src.common.utils as utils

class init_value():
    def init(self):
        # Common
        self.debug = True  # 이미지 Log를 볼때 사용한다.
        self.gallery_load_flag = True

        self.rotation = False

        self.detect_type = 'mtcnn' # dlib, mtcnn, hog, cnn
        self.pair_type = 'svm'  # svm, svm_pair, cnn_pair, distance_sub, distance_cos

        self.project_dir = os.path.dirname(os.path.abspath(__file__)) + '/'
        self.gpu_memory_fraction = 0.5
        self.minsize = 20 # minimum size of face
        self.threshold = [0.6, 0.7, 0.7] # three steps's threshold
        self.factor = 0.9 # scale factor 0.709
        self.margin = 0
        self.batch_size = 70
        self.image_size = 160
        self.cropped_size = 25  # rotation use
        self.seed = 666

        # Make Directory
        feature_cnt = ''
        train_cnt = ''
        eval_cnt = ''
        gallery_cnt = ''

        self.pre_data_dir = self.project_dir + 'data/'
        self.pre_datatxt_dir = self.project_dir + 'datatxt/'
        self.feature_dir = utils.make_dir(self.pre_data_dir + '/feature_data' + feature_cnt + '/')
        self.feature_detect_dir = utils.make_dir(self.pre_data_dir + '/feature_detect' + feature_cnt + '/')
        self.feature_rotation_dir = utils.make_dir(self.pre_data_dir + '/feature_rotation' + feature_cnt + '/')
        self.train_dir = utils.make_dir(self.pre_data_dir +'/train_data'+train_cnt+'/')
        self.train_detect_dir = utils.make_dir(self.pre_data_dir +'/train_detect'+train_cnt+'/')
        self.train_rotation_dir = utils.make_dir(self.pre_data_dir +'/train_rotation'+train_cnt+'/')
        self.eval_dir = utils.make_dir(self.pre_data_dir +'/eval_data'+eval_cnt+'/')
        self.eval_detect_dir = utils.make_dir(self.pre_data_dir +'/eval_detect'+eval_cnt+'/')
        self.eval_rotation_dir = utils.make_dir(self.pre_data_dir +'/eval_rotation'+eval_cnt+'/')
        self.gellery_dir = utils.make_dir(self.pre_data_dir + 'gallery_data'+gallery_cnt+'/')
        self.gallery_detect_dir = utils.make_dir(self.pre_data_dir + 'gallery_detect'+gallery_cnt+'/')
        self.gallery_rotation_dir = utils.make_dir(self.pre_data_dir + 'gallery_rotation'+gallery_cnt+'/')
        self.lfw_dir = utils.make_dir(self.pre_data_dir + 'lfw/')
        self.lfw_detect_dir = utils.make_dir(self.pre_data_dir + 'lfw_mtcnnpy_160')
        self.lfw_rotation_dir = utils.make_dir(self.pre_data_dir + 'lfw_mtcnnpy_rotation_160')

        self.pre_model_dir = utils.make_dir(self.project_dir + 'pre_model/')

        self.save_dir = utils.make_dir('/hoya_src_root/save_data/')
        self.log_dir = utils.make_dir('/hoya_src_root/log_data/')

        # Model
        self.pretrained_model_dir = '20170512-110547'
        self.pretrained_model = self.pre_model_dir + self.pretrained_model_dir + '/' + self.pretrained_model_dir + '.pb'
        if not os.path.exists(self.pretrained_model):
            download_and_extract.download_and_extract_file(self.pretrained_model_dir, self.pre_model_dir)

        self.feature_model_dir = '20170512-110547' #'20180212-062537' #'20180207-000626' #'20170512-110547'
        self.feature_model = self.pre_model_dir + self.feature_model_dir + '/' + self.feature_model_dir + '.pb'

        self.predictor_68_face_landmarks = 'shape_predictor_68_face_landmarks.dat.bz2'
        utils.shape_predictor_68_face_landmarks_download(self.pre_model_dir, self.predictor_68_face_landmarks)

        # file name
        self.classifier_filename = self.pre_model_dir + self.feature_model_dir+'_my_classifier_'+self.pair_type+'.pkl'+train_cnt
        self.gallery_filename = self.pre_model_dir + self.feature_model_dir + '_gallery'+gallery_cnt
        self.gallery_train = self.pre_model_dir + self.feature_model_dir + '_gallery' + '_train'+eval_cnt
        self.gallery_eval = self.pre_model_dir + self.feature_model_dir + '_gallery' + '_eval' + eval_cnt
        self.font_location = self.project_dir + 'font/ttf/NanumBarunGothic.ttf'

        #lfw
        self.lfw_pairs = self.pre_datatxt_dir + 'pairs.txt'
        self.lfw_file_ext='png'
        self.lfw_batch_size=100
        self.lfw_nrof_folds=10

