from grade_analysis import analysis, file_io

origion_file = 'students.csv'
result_file = 'result.csv'
stu_data = []

    
def main():
    try:
        file_io.read_data(origion_file, stu_data)
        
        data1 = analysis.ahl_score(stu_data)

        data2 = analysis.total_rank3(stu_data)

        data3 = analysis.failed_list(stu_data)

        file_io.write_data(result_file, data1, data2, data3)

    except Exception as e:
        print(f"Error: {e}")


main()



    
