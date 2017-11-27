from facenet_realtime import init_value
from facenet_realtime.src.align.align_dataset_mtcnn import AlignDatasetMtcnn
from facenet_realtime.src.align.align_dataset_rotation import AlignDatasetRotation
from facenet_realtime.src.common.classifier import ClassifierImage


class Facenet_run():
    def run(self):
        init_value.init_value.init(self)

        # object detect
        AlignDatasetMtcnn().align_dataset(self.train_data_path, self.detect_data_path, True)

        # object rotate detect
        AlignDatasetRotation().rotation_dataset(self.train_data_path, self.rotate_data_path, True)
        AlignDatasetMtcnn().align_dataset(self.rotate_data_path, self.rotdet_data_path, False)

        # classifier Train
        ClassifierImage().classifier_dataset(self.detect_data_path, self.model_name_detect)

        # classifier Train
        ClassifierImage().classifier_dataset(self.rotdet_data_path, self.model_name_rotdet)

if __name__ == '__main__':
    Facenet_run().run()


