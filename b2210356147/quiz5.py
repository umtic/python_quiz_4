import os,sys,os.path
current_dir_path=os.getcwd()
def fread():
    global calc
    calc=[]
    global comp
    comp=[]
    try:
        try:
            x=sys.argv[1]
            os.path.exists(x) is True
            reading_file_name=x
            reading_file_path=os.path.join(current_dir_path,reading_file_name)
            with open(reading_file_path,"r") as i:
                count=0
                while True:
                    count+=1
                    line=i.readline()
                    if not line:
                        break
                    calc+=line.splitlines()
            i.close()
        except IOError:
            print("IOError: cannot open {}.".format(x))
        try:
            y=sys.argv[2]
            os.path.exists(y) is True
            reading_file_name=y
            reading_file_path=os.path.join(current_dir_path,reading_file_name)
            with open(reading_file_path,"r") as i:
                count=0
                while True:
                    count+=1
                    line=i.readline()
                    if not line:
                        break
                    comp+=line.splitlines()
                i.close()   
        except IOError:
            print("IOError: cannot open {}.".format(y))
    except IndexError:
        print("Index Error: number of input files less than expected.")
def calculate():
    strresult=""
    for i in range(len(calc)):
        if len(comp)==0:
            break
        else:
            try:
                strcalc=calc[i].split(" ")
                div=float(strcalc[0])
                nondiv=float(strcalc[1])
                sfrom=float(strcalc[2])
                to=float(strcalc[3])
                if div is not int:
                    div=round(div)
                if nondiv is not int:
                    nondiv=round(nondiv)
                if sfrom is not int:
                    sfrom=round(sfrom)
                if to is not int:
                    to=round(to)
                for j in range(sfrom,to+1):
                    if j%div==0:
                        if j%nondiv!=0:
                            strresult+=str(j)
                            strresult+=" "
                strresult=strresult[:-1]
                strresult+="\n"
                result=list(strresult.split("\n"))
                result.pop()
                assert result[-1]==comp[i]
                print("------------")
                print("My results:\t\t{}".format(result[-1]))
                print("Results to compare:\t{}".format(comp[i]))
                print("Goool!!!")
            except IndexError:
                print("------------")
                print("IndexError: number of operands less than expected.")
                print("Given input: {}".format(calc[i]))
            except ValueError:
                print("------------")
                print("ValueError: only numeric input is accepted.")
                print("Given input: {}".format(calc[i]))
            except ZeroDivisionError:
                print("------------")
                print("ZeroDivisionError: You can't divide by 0.")
                print("Given input: {}".format(calc[i]))
            except AssertionError:
                print("------------")
                print("My results:\t\t{}".format(result[-1]))
                print("Results to compare:\t{}".format(comp[i]))                
                print("Assertion Error: results don't match.")
try:
    fread()
    calculate()
except Exception as e:
    print("kaBOOM: run for your life!\n",e)
finally:
        print("\n~Game Over~")