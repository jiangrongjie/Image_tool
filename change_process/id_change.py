import os

def modify_labels_based_on_error_images(error_image_dir, label_dir, old_class_id, new_class_id):
    # 获取错误图片文件名列表（不包括扩展名）
    error_image_files = [os.path.splitext(f)[0] for f in os.listdir(error_image_dir) if f.endswith(('.jpg', '.png'))]

    for error_image_file in error_image_files:
        label_file = f"{error_image_file}.txt"  # 对应的标签文件名
        label_path = os.path.join(label_dir, label_file)

        # 检查标签文件是否存在
        if os.path.exists(label_path):
            # 读取标签文件的内容
            with open(label_path, 'r') as f:
                lines = f.readlines()

            # 修改标签文件中的类别ID
            modified_lines = []
            for line in lines:
                elements = line.strip().split()
                class_id = int(elements[0])  # 获取类别ID

                # 如果类别ID等于 old_class_id，则替换为 new_class_id
                if class_id == old_class_id:
                    elements[0] = str(new_class_id)

                # 重新组合行
                modified_line = " ".join(elements)
                modified_lines.append(modified_line)

            # 将修改后的内容写回文件
            with open(label_path, 'w') as f:
                f.write("\n".join(modified_lines) + "\n")

            print(f"Modified: {label_file}")
        else:
            print(f"Label file not found for: {error_image_file}")

# 设置错误图片文件夹路径和标签文件夹路径
error_image_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/output1/class_0/8" # 错误图片文件夹路径
label_directory = "/home/jrj/python3.8/bin/Yolo-FastestV2/data/bidata_pro/labels/train"  # 标签文件夹路径
old_class_id = 0  # 旧的类别ID
new_class_id = 8  # 新的类别ID

# 运行函数
modify_labels_based_on_error_images(error_image_directory, label_directory, old_class_id, new_class_id)

