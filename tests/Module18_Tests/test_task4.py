from Module18_Tasks.Task4.Task4 import Task4

def test_is_ip_correct():
    ip1 = "128.0.0.255"
    ip2 = "240.127.56.340"
    ip3 = "192.c8.1.10"
    task = Task4()
    assert task.is_ip_correct(ip1) == True
    assert task.is_ip_correct(ip2) == False
    assert task.is_ip_correct(ip3) == False

def test_is_files_correct():
    files1 = "file_1.txt document_2024.docx notes2022.txt"
    files2 = "file_21.txt @data_report.txt notes2024.txt"
    files3 = "file.txt analysis_results.ttx notes2000.txt"
    task = Task4()
    assert task.is_files_correct(files1) == True
    assert task.is_files_correct(files2) == False
    assert task.is_files_correct(files3) == False

def test_get_correct_info():
    data = [
        ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
        ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
        ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
        ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
        ["192.168.1.10", ["file_432.txt important_info.txt notes1900.txt"]],
        ["192.c8.1.10", ["file_432.xt &meeting_notes.docx notes1995.txt"]],
        ["10.20.30.40", ["file_432.txt analysis_results.txt notes1998.txt"]]]
    task = Task4()
    assert task.get_correct_info(data) == [['128.0.0.255', ['file_1.txt document_2024.docx notes2022.txt']], 
                                           ['192.168.1.10', ['file_432.txt important_info.txt notes1900.txt']], 
                                           ['10.20.30.40', ['file_432.txt analysis_results.txt notes1998.txt']]]