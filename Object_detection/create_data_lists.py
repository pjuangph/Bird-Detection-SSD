from utils import create_data_lists

if __name__ == '__main__':
    create_data_lists(voc07_path='VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007',
                      voc12_path='VOCtrainval_11-May-2012/VOCdevkit/VOC2012',
                      test_path='VOCtest_06-Nov-2007/VOCdevkit/VOC2007',
                      output_folder='./')
