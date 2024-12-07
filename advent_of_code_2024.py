import re



#Advent of Code

class Calendar():
    def __init__(self, day:int, input=None) -> None:
        day = str(day)
        function_dict = {"1":self.day1, "2":self.day2, "3":self.day3}

        function_dict[day]()
        

    def day1(self, input=None):
        #Day 1
        text_file = "day1.txt"
        sum = 0
        str_list1 = []
        str_list2 = []

        with open(text_file, "r") as file:
                for line in file:
                        current_line = line.split()
                        str_list1.append(current_line[0])
                        str_list2.append(current_line[1])
        file.close()

        self.list1 = [int(i) for i in str_list1]
        self.list2 = [int(i) for i in str_list2]

        self.list1.sort()
        self.list2.sort()
        length = len(self.list1)

        for i in range(length):
            item1 = self.list1[i] 
            item2 = self.list2[i]
            distance = abs(item1 - item2)
            sum += distance

        print(sum)
        print("done")
        


    def day2(self):
        self.day1()
        similarity_score = 0
        for value in self.list1:
            similarity_value = self.similarity_value(value, self.list2)
            similarity_score += similarity_value

        print(similarity_score)
         
    
    def similarity_value(self, value:int, location_list:list, ) -> int:
        #Called for Day 2
        count = location_list.count(value)
        similarity_value = value * count
        return similarity_value
    

    def day2(self) -> int:
        reports = self.list_from_txt_input("day2.txt")
        safe_reports = 0
        for report in reports:
            report_list = report.split()
            if self.check_report(report_list):
                safe_reports+=1
            else:
                if self.check_report_with_dampener(report_list):
                    safe_reports+=1

        print("part 1: ", safe_reports)
        



    def list_from_txt_input(self, path:str) -> list:
        output = []
        with open(path, "r") as file:
            for line in file:
                output.append(line)
        file.close()

        return output
    
    def check_report(self, report:list[str], dampener:bool) -> bool:
        #Called by day 2
        report = [int(i) for i in  report]

        ascending_report = report.copy()
        ascending_report.sort()

        descending_report = report.copy()
        descending_report.sort(reverse=True)
        
        if report != ascending_report and report != descending_report:
            return False
        
        for i in range(1,len(report)):
            difference = abs(report[i] - report[i-1])
            if difference >= 1 and difference <= 3:
                continue
            else:
                return False
        
        print(report)
        return True
    
    def check_report_with_dampener(self, report:list[str]) -> bool:
        report = [int(i) for i in  report]
        ascending = []
        error_count = 0
        for i in range(1,len(report)):
            difference = report[i] - report[i-1]
            if difference > 0:
                ascending.append(True)
            else:
                ascending.append(False)

            if abs(difference) >= 1 and abs(difference) <= 3:
                continue
            else:
                error_count+=1
        
        if all(ascending):
            pass
        else:
            pass

        
        print(report)
        return True
    
    def day3(self):
        text_list = self.list_from_txt_input("day3.txt")
        text = text_list[0]
        mul_pattern = "mul\(\d+,\d+\)"
        mul_list = self.find_muls(mul_pattern, text)

        total = 0

        for mul in mul_list:
            string_value = self.numbers_from_string(mul)
            value = self.process_numbers(string_value)
            total+=value
        
        print(total)


    def process_numbers(self, numbers:list[str]) -> int:
        values = [int(number) for number in numbers]
        total = 0
        for number in values:
            if total == 0:
                total = number
            else:
                total*=number
        return total
        
    def numbers_from_string(self, string:str) -> list:
        pattern = "\((\d+),\s*(\d+)\)"
        matches = re.findall(pattern, string)
        output = list(matches[0])
        return output

    def find_muls(self, pattern:str, text:str) -> list:
        output = re.findall(pattern=pattern, string=text)
        return output


calendar = Calendar(day=3)




