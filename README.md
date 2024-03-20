Các bước để deploy app lên cloud
B1: Tạo tk Github và tk Streamlit cloud
B2: Liên kết Streamlit cloud và Github
B3: Tạo mới 1 Repo trên Github: Upload file python Iris Classifier đã hoàn thiện trên lớp
B4: Trên trang Streamlit cloud ấn vào mục New app, điền các thông tin theo yêu cầu, bao gồm: Tên Repo, Branch (main) và Main file path, sau đó chọn Deploy
B5: Hệ thống sẽ tạo 1 máy chủ mới (với domain name là random_string.streamlit.app) để deploy app
    Đợi hệ thống biên dịch xong sẽ cho kết quả ra màn hình
    Có thể check nhật ký deploy qua mục ManageApp
**Notes: Bài của e đã hoàn thành đến bước delpoy, tuy nhiên hệ thống báo lỗi bên dưới, và e ko biết cách fix :(((
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/st-hello-word-/testAI.py", line 3, in <module>
    from sklearn.datasets import load_iris
