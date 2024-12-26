import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox
from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录")  # 窗口标题
        self.setFixedSize(350, 270)  # 固定窗口大小

        # 创建组件
        self.username_label = QLabel("用户名：")
        self.password_label = QLabel("密码：")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # 设置密码输入框为密码模式
        self.login_button = QPushButton("登录")
        self.remember_checkbox = QCheckBox("记住密码")  # 记住密码的复选框
        self.register_button = QPushButton("注册")  # 注册按钮

        # 布局
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        # 将组件添加到布局
        self.form_layout.addWidget(self.username_label)
        self.form_layout.addWidget(self.username_input)
        self.form_layout.addWidget(self.password_label)
        self.form_layout.addWidget(self.password_input)
        self.form_layout.addWidget(self.remember_checkbox)  # 添加复选框

        self.button_layout.addWidget(self.login_button)
        self.button_layout.addWidget(self.register_button)  # 添加注册按钮

        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)

        # 设置窗口布局
        self.setLayout(self.layout)

        # 信号连接
        self.login_button.clicked.connect(self.handle_login)
        self.register_button.clicked.connect(self.open_registration_page)  # 连接注册按钮到跳转方法

        # 应用 QSS 样式
        self.apply_styles()

        # 加载已保存的用户名和密码
        self.load_credentials()

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # 获取复选框状态，决定是否记住密码
        remember_password = self.remember_checkbox.isChecked()

        if not username or not password:
            self.show_message("错误", "用户名和密码不能为空！", QMessageBox.Critical)
            return

        # 向后端发送 POST 请求进行登录验证
        url = "http://localhost:8000/api/accounts/login/"  # 你的后端 API 地址
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                self.show_message("成功", "登录成功！", QMessageBox.Information)
                if remember_password:
                    self.save_credentials(username, password)  # 保存用户名和密码
            else:
                error_message = response.json().get("detail", "登录失败，请检查用户名和密码。")
                self.show_message("错误", error_message, QMessageBox.Critical)
        except requests.exceptions.RequestException as e:
            self.show_message("错误", f"请求失败: {e}", QMessageBox.Critical)

    def save_credentials(self, username, password):
        """保存用户名和密码"""
        settings = QSettings("MyCompany", "MyApp")  # 用于保存配置的实例
        settings.setValue("username", username)
        settings.setValue("password", password)
        settings.setValue("remember_password", True)

    def load_credentials(self):
        """加载保存的用户名和密码"""
        settings = QSettings("MyCompany", "MyApp")
        if settings.contains("username") and settings.contains("password"):
            self.username_input.setText(settings.value("username"))
            self.password_input.setText(settings.value("password"))
            self.remember_checkbox.setChecked(True)  # 默认勾选记住密码

    def open_registration_page(self):
        """打开注册页面链接"""
        registration_url = "https://www.example.com/register"  # 替换为你的注册页面链接
        QDesktopServices.openUrl(QUrl(registration_url))

    def show_message(self, title, message, icon):
        """显示消息框"""
        msg = QMessageBox(self)
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()

    def apply_styles(self):
        # 设置 QSS 样式
        qss = """
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }

            QLabel {
                color: #333333;
                font-weight: bold;
            }

            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                margin-bottom: 10px;
            }

            QLineEdit:focus {
                border-color: #0078d4;
            }

            QPushButton {
                background-color: #0078d4;
                color: white;
                border-radius: 5px;
                padding: 10px 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #005a8d;
            }

            QPushButton:pressed {
                background-color: #003f69;
            }

            QPushButton:disabled {
                background-color: #cccccc;
                color: #888888;
            }

            QCheckBox {
                color: #333333;
                font-size: 12px;
                margin-top: 10px;
            }

            QHBoxLayout {
                spacing: 10px;
                margin-top: 10px;
            }

            QVBoxLayout {
                spacing: 20px;
                padding: 20px;
            }
        """
        # 应用样式表
        self.setStyleSheet(qss)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
