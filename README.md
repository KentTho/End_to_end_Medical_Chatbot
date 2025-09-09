Chào bạn, dưới đây là phiên bản tệp `README.md` được viết lại, tóm tắt thông tin từ các nguồn đã cung cấp và cuộc trò chuyện của chúng ta về dự án chatbot y tế.

---

# Dự án Chatbot Y tế Toàn diện | Generative AI

## Giới thiệu
Chào mừng bạn đến với dự án chatbot y tế toàn diện sử dụng Generative AI! Dự án này triển khai một chatbot y tế đầu cuối có khả năng cung cấp các gợi ý về chẩn đoán, thuốc men và các thông tin y tế khác dựa trên các truy vấn của người dùng. Mục tiêu là xây dựng một hệ thống hoàn chỉnh bao gồm giao diện người dùng (frontend) và quy trình xử lý dữ liệu (backend) sử dụng mã nguồn mô-đun trong Python.

## Tính năng chính
*   **Dữ liệu tùy chỉnh**: Sử dụng dữ liệu y tế tùy chỉnh từ một cuốn sách y tế lớn ("The G Encyclopedia of Medicine Second Edition" với 637 trang) để xây dựng cơ sở tri thức.
*   **Cơ sở tri thức dựa trên Vector**: Xây dựng cơ sở tri thức bằng cách trích xuất thông tin, tạo các đoạn văn bản (chunks), tạo nhúng vector (vector embeddings) và lưu trữ chúng trong cơ sở dữ liệu vector đám mây **Pinecone**.
*   **Tích hợp Mô hình ngôn ngữ lớn (LLM)**: Sử dụng **OpenAI LLM** để xử lý các truy vấn của người dùng, kết hợp với thông tin từ cơ sở tri thức để đưa ra phản hồi chính xác và liên quan.
*   **Giao diện người dùng thân thiện**: Phát triển giao diện người dùng đẹp mắt cho chatbot bằng **Flask**, HTML và CSS, cho phép người dùng dễ dàng nhập câu hỏi và nhận câu trả lời.
*   **Mã hóa mô-đun**: Toàn bộ dự án được triển khai bằng cách sử dụng các khái niệm mã hóa mô-đun trong Python, giúp tổ chức mã nguồn sạch sẽ, dễ quản lý và bảo trì.
*   **Kiểm soát phiên bản**: Sử dụng **Git** và **GitHub** để kiểm soát phiên bản và quản lý quá trình phát triển.
*   **Triển khai đám mây**: Dự án có kế hoạch triển khai lên nền tảng đám mây **AWS**, bao gồm cả triển khai đơn giản và triển khai CI/CD.

## Công nghệ được sử dụng
*   **Mô hình ngôn ngữ lớn (LLM)**: OpenAI LLM
*   **Khung phát triển Generative AI**: LangChain
*   **Cơ sở dữ liệu Vector**: Pinecone (đám mây)
*   **Khung ứng dụng web**: Flask (Python)
*   **Ngôn ngữ lập trình**: Python
*   **Kiểm soát phiên bản**: Git và GitHub
*   **Tải dữ liệu PDF**: `pypdf`, `PyPDFLoader`, `DirectoryLoader`
*   **Chia đoạn văn bản**: `RecursiveCharacterTextSplitter`
*   **Mô hình nhúng**: Hugging Face embedding model (ví dụ: `all-MiniLM-L6-v2`)
*   **Quản lý biến môi trường**: `python-dotenv`

## Kiến trúc dự án
Quy trình xử lý của chatbot y tế bao gồm các bước sau:
1.  **Trích xuất dữ liệu**: Thông tin y tế từ tệp PDF (`The G Encyclopedia of Medicine Second Edition.pdf`) được trích xuất.
2.  **Chia đoạn văn bản**: Dữ liệu đã trích xuất được chia thành các đoạn văn bản nhỏ (chunks) để phù hợp với giới hạn đầu vào của LLM.
3.  **Tạo nhúng Vector**: Một mô hình nhúng (embedding model) từ Hugging Face được sử dụng để chuyển đổi các đoạn văn bản thành các nhúng vector.
4.  **Xây dựng cơ sở tri thức**: Các nhúng vector này được lưu trữ vào cơ sở dữ liệu vector **Pinecone**, tạo thành cơ sở tri thức của chatbot.
5.  **Xử lý truy vấn**: Khi người dùng nhập câu hỏi vào giao diện người dùng, truy vấn đó sẽ được chuyển đổi thành nhúng vector và được sử dụng để tìm kiếm ngữ nghĩa (semantic search) trong cơ sở dữ liệu Pinecone để tìm các đoạn văn bản liên quan nhất.
6.  **Tạo phản hồi**: Truy vấn của người dùng cùng với các đoạn văn bản liên quan được truy xuất từ Pinecone (làm ngữ cảnh) và một "system prompt" được gửi đến **OpenAI LLM**. LLM sau đó sẽ xử lý thông tin này và tạo ra một phản hồi chính xác và mạch lạc.
7.  **Giao diện người dùng**: Ứng dụng Flask cung cấp một giao diện web, hiển thị các phản hồi của chatbot cho người dùng.

## Hướng dẫn cài đặt
Để thiết lập và chạy dự án này trên máy cục bộ của bạn, hãy làm theo các bước dưới đây:

### 1. Clone Repository
Mở terminal hoặc Git Bash và clone repository này về máy của bạn:
```bash
git clone <repository_link>
cd end-to-end-medical-chatbot-gen-ai # Tên thư mục dự án
```


### 2. Tạo môi trường ảo
Sử dụng `conda` để tạo một môi trường ảo mới với Python 3.10:
```bash
conda create -p medibot python==3.10 -y
```
Bạn có thể thay thế `medibot` bằng tên môi trường ảo khác nếu muốn.

### 3. Kích hoạt môi trường ảo
Kích hoạt môi trường ảo đã tạo:
```bash
conda activate medibot
```


### 4. Tạo tệp `.env`
Tạo một tệp có tên `.env` trong thư mục gốc của dự án. Tệp này sẽ chứa các khóa API nhạy cảm của bạn.
Thêm các biến môi trường sau vào tệp `.env`:
```
OPENAI_API_KEY="your_openai_api_key_here"
PINECONE_API_KEY="your_pinecone_api_key_here"
PINECONE_API_ENV="us-west-1" # hoặc môi trường Pinecone của bạn (ví dụ: gcp-starter, aws-us-east-1)
```
Thay thế `"your_openai_api_key_here"`, `"your_pinecone_api_key_here"` và `"us-west-1"` bằng khóa API và môi trường Pinecone thực tế của bạn.

### 5. Tạo cấu trúc thư mục dự án
Chạy tệp `template.py` để tự động tạo cấu trúc thư mục và tệp cần thiết cho dự án:
```bash
python template.py
```


### 6. Cài đặt các thư viện phụ thuộc
Cài đặt tất cả các thư viện Python cần thiết được liệt kê trong `requirements.txt`:
```bash
pip install -r requirements.txt
```
Các thư viện bao gồm `sentence-transformers`, `langchain`, `Flask`, `pypdf`, `python-dotenv`, `pinecone-client`, `pinecone-grcp`, `langchain-pinecone`, `langchain-community`, `langchain-openai`, `langchain-experimental`.

### 7. Thiết lập dự án như một gói cục bộ
Chạy lệnh sau để thiết lập dự án của bạn như một gói Python cục bộ, cho phép import các mô-đun từ thư mục `src`:
```bash
pip install -e .
```


## Chạy ứng dụng
Sau khi cài đặt xong, bạn có thể chạy ứng dụng theo hai bước:

### 1. Xây dựng cơ sở tri thức (Knowledge Base)
Chạy script `store_index.py` để trích xuất dữ liệu từ PDF, tạo nhúng vector và lưu trữ chúng vào cơ sở dữ liệu Pinecone. Bước này chỉ cần thực hiện một lần ban đầu hoặc khi có dữ liệu mới cần cập nhật.
```bash
python store_index.py
```
Quá trình này sẽ:
*   Tải dữ liệu PDF y tế từ thư mục `data`.
*   Chia dữ liệu thành các đoạn văn bản (chunks).
*   Tải mô hình nhúng từ Hugging Face.
*   Tạo một chỉ mục (index) Pinecone (ví dụ: `medical-bot`).
*   Tạo các nhúng vector từ các đoạn văn bản và lưu trữ chúng vào chỉ mục Pinecone.

### 2. Khởi động ứng dụng Chatbot
Chạy tệp `app.py` để khởi động ứng dụng web Flask:
```bash
python app.py
```
Lệnh này sẽ khởi động máy chủ web Flask, tải mô hình nhúng, kết nối với chỉ mục Pinecone và LLM của OpenAI, sau đó render giao diện người dùng.

### 3. Truy cập Chatbot
Mở trình duyệt web của bạn và truy cập địa chỉ sau:
```
http://127.0.0.1:8080
```
Bạn sẽ thấy giao diện người dùng chatbot và có thể bắt đầu tương tác.

## Triển khai (Kế hoạch tương lai)
Chúng tôi sẽ sớm cung cấp hướng dẫn về cách triển khai dự án này lên nền tảng đám mây AWS, bao gồm cả các phương pháp triển khai đơn giản và CI/CD.

## Đóng góp và Hỗ trợ
Nếu bạn thấy dự án này hữu ích, hãy đánh dấu sao (star) và fork repository này để có thể tham khảo trong tương lai. Mọi đóng góp đều được hoan nghênh!

---