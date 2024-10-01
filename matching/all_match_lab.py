import os
import cv2

def draw_yolo_boxes(image_dir, label_dir, output_dir):
    # 检查输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取图像文件和标签文件
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    for image_file in image_files:
        # 获取图像名
        image_name = os.path.splitext(image_file)[0]
        label_file = f"{image_name}.txt"

        # 如果有匹配的标签文件
        if label_file in label_files:
            # 读取图像
            image_path = os.path.join(image_dir, image_file)
            image = cv2.imread(image_path)

            # 获取图像的宽度和高度
            h, w, _ = image.shape

            # 读取YOLO格式的标签文件
            label_path = os.path.join(label_dir, label_file)
            with open(label_path, 'r') as f:
                labels = f.readlines()

            # 遍历每一行标签
            for label in labels:
                # YOLO格式：class_id, x_center, y_center, width, height
                class_id, x_center, y_center, width, height = map(float, label.strip().split())

                # 将归一化的YOLO坐标转换为图像中的像素坐标
                x_center_pixel = int(x_center * w)
                y_center_pixel = int(y_center * h)
                width_pixel = int(width * w)
                height_pixel = int(height * h)

                # 计算矩形框的左上角和右下角坐标
                x1 = int(x_center_pixel - width_pixel / 2)
                y1 = int(y_center_pixel - height_pixel / 2)
                x2 = int(x_center_pixel + width_pixel / 2)
                y2 = int(y_center_pixel + height_pixel / 2)

                # 绘制矩形框
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 使用绿色框，线宽为2
                # 添加类别索引标签到矩形框的左上角
                cv2.putText(image, str(int(class_id)), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # 保存标注后的图片到输出文件夹
            output_image_path = os.path.join(output_dir, image_file)
            cv2.imwrite(output_image_path, image)

            print(f"Processed: {image_file}")

# 设置文件夹路径
image_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/images/train"  # 图像文件夹路径
label_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/labels/train"  # 标签文件夹路径
output_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/output"  # 输出文件夹路径

# 运行函数
draw_yolo_boxes(image_directory, label_directory, output_directory)

