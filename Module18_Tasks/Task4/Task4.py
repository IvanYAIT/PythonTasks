class Task4:
    def is_ip_correct(self, ip):
        ip_list = ip.split(".")
        try:
            for ip_part in ip_list:
                if(int(ip_part) < 0 or int(ip_part) > 255):
                    return False
        except:
            return False
        
        return True
        
    def is_files_correct(self, files):
        INCORRECT_SYMBOLS = "@№$%^&*()"
        file_list = files.split(" ")
        for file in file_list:
            for symbol in INCORRECT_SYMBOLS:
                if(symbol == file[0]):
                    return False
            if(file[len(file):len(file)-4:-1] != "txt" 
               and file[len(file):len(file)-5:-1] != "xcod"):
                return False
                
        return True

    def get_correct_info(self, data):
        result = []
        for info in data:
            if (self.is_ip_correct(info[0]) and self.is_files_correct(info[1][0])):
                result.append(info) 
        return result
    
    def main(self):
        data = [
            ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
            ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
            ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
            ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
            ["192.168.1.10", ["file_432.txt important_info.txt notes1900.txt"]],
            ["192.c8.1.10", ["file_432.xt &meeting_notes.docx notes1995.txt"]],
            ["10.20.30.40", ["file_432.txt analysis_results.txt notes1998.txt"]]]
        correct_data = self.get_correct_info(data)
        for info in correct_data:
            print(info)