import os
import shutil

def classify_images_and_labels(image_dir, label_dir, output_base_dir):
    # 检查输出的基文件夹是否存在，不存在则创建
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    # 获取图像文件和标签文件
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    for image_file in image_files:
        # 获取图像名
        image_name = os.path.splitext(image_file)[0]
        label_file = f"{image_name}.txt"

        # 如果有匹配的标签文件
        if label_file in label_files:
            # 读取标签文件中的类别
            label_path = os.path.join(label_dir, label_file)
            with open(label_path, 'r') as f:
                labels = f.readlines()

            # 假设每张图像只属于一个类别，取第一个类别
            if labels:
                first_label = labels[0].strip().split()[0]  # 获取第一个标签的类别id
                class_id = int(first_label)  # 转换为整数表示类别id

                # 创建类别文件夹
                class_folder = os.path.join(output_base_dir, f"class_{class_id}")
                if not os.path.exists(class_folder):
                    os.makedirs(class_folder)

                # 将图像和标签文件复制到对应类别文件夹中
                src_image_path = os.path.join(image_dir, image_file)
                src_label_path = os.path.join(label_dir, label_file)

                dst_image_path = os.path.join(class_folder, image_file)
                dst_label_path = os.path.join(class_folder, label_file)

                shutil.copy(src_image_path, dst_image_path)
                shutil.copy(src_label_path, dst_label_path)

            print(f"Processed: {image_file} -> class_{class_id}")

# 设置文件夹路径
image_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/images/train"  # 图像文件夹路径
label_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/labels/train"  # 标签文件夹路径
output_base_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/output2"  # 输出的基文件夹路径

# 运行函数
classify_images_and_labels(image_directory, label_directory, output_base_directory)

