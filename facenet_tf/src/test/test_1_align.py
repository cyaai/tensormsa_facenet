from facenet_tf import init_value
from facenet_tf.src.align.align_dataset_mtcnn import main as align_main

class Facenet_run():
    def run(self):
        init_value.init_value.init(self)

        self.random_order = False  # random.shuffle(dataset)
        self.detect_multiple_faces = False
        ####################################################
        # Train Data Detect & Rotation
        self.input_dir = self.eval_dir
        self.output_dir = self.eval_detect_dir
        if self.rotation == True:
            self.output_dir = self.train_rotation_dir

        align_main(self)

if __name__ == '__main__':
    Facenet_run().run()