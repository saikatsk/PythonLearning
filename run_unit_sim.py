import argparse
import os

def prepare_cdslib():
    write_file = open("cdstop.lib", mode='w')
    write_file.write("SOFTINCLUDE                          $CDS_LIB_FILE" + os.linesep);
    write_file.write("DEFINE INI_CAN                       $LIB_DIR/$testcase/iuswork/worklib" + os.linesep);
    write_file.write("DEFINE GLOBAL                        $LIB_DIR/$testcase/iuswork/worklib" + os.linesep);
    write_file.close()

def create_seq_lib():
    pwd = os.getcwd()
    print("Present working dir: " + pwd)
    write_file = open("unit_seq_lib.svh", mode='w')
    # Get file list from directory
    files = os.listdir(pwd)
    for f in files:
        # Get each file name
        file_name = str(f)
        # Split file name from extension
        str_split = file_name.split(".", 50)
        # Following prints are for debug purpose only
        print(file_name)
        print(str_split[0])
        # Look for file extension (.svh for sequences)
        if (str_split[1] == "py"):
            write_file.write("#ifdef " + str_split[0] + os.linesep)
            write_file.write("\t" + "#include " + str_split[0] + ".svh" + os.linesep)
            write_file.write("#endif" + os.linesep)

    write_file.close()

def parse_command_line():
    parser = argparse.ArgumentParser("run_unit_sim.py")
    parser.add_argument('--top',
        help='Usage: --top < Top level design unit name (DUT)>')
    parser.add_argument('--test_name',
        help='Usage: --test_name < Test name: test to run >')
    parser.add_argument('--uvm_verbosity',
        choices= ['UVM_DEBUG', 'UVM_FULL', 'UVM_HIGH', 'UVM_LOW', 'UVM_MEDIUM', 'UVM_NONE'],
        help='Usage: --uvm_verbosity < UVM_DEBUG | UVM_FULL | UVM_HIGH | UVM_LOW | UVM_MEDIUM | UVM_NONE >')
    parser.add_argument('--uvm_timeout',
        help='Usage: --uvm_timeout < UVM Test timeout value >')
    parser.add_argument('--svseed',
        help='Usage: --svseed < UVM Test seed >')
    parser.add_argument('--DEFINE', nargs='+',
        help='Usage: --DEFINE < define(s) to pass to test bench>')
    parser.add_argument('--sixty_four', action='store_true',
        help='To enable XRUN run on 64 bit mode')
    parser.add_argument('--notimingchecks', action='store_true',
        help='Pass -notimingchecks option to XRUN')
    parser.add_argument('--nospecify', action='store_true',
        help='Pass -nospecify option to XRUN')
    parser.add_argument('--fast_func', action='store_true',
        help='Define and pass -fast_func option to XRUN')

    args = parser.parse_args()
    #print(args)
    write_file = open("xrun_args.arg", mode='w')
    write_file.write("-top " + str(args.top) + os.linesep)
    write_file.write("+UVM_TESTNAME=" + str(args.test_name) + os.linesep)
    print("Argument DEFINE value is: " + str(args.DEFINE))
    collected_defines = args.DEFINE
    print(collected_defines)
    if (args.DEFINE != None):
        len_defines = len(collected_defines)
        print("Number of defines supplied: " + str(len_defines))
        for i in range(len_defines):
            write_file.write("-define " + args.DEFINE[i] + os.linesep)

    if (args.sixty_four == True):
        print("XRUN 64bit mode enabled.")
        write_file.write("-64bit" + os.linesep)

    write_file.write("-v93" + os.linesep)
    write_file.write("-nocopyright" + os.linesep)
    write_file.write("-access +rwc" + os.linesep)
    write_file.write("-nclibdirname $LIB_DIR/$testcase/iuswork" + os.linesep)
    write_file.write("-cdslib $LIB_DIR/$testcase/iuswork/cdstop.lib" + os.linesep)
    write_file.write("-timescale 1ns/1ps" + os.linesep)

    if (args.notimingchecks == True):
        write_file.write("-notimingchecks" + os.linesep)

    if (args.nospecify == True):
        write_file.write("-nospecify" + os.linesep)

    write_file.write("-no_tchk_msg" + os.linesep)
    write_file.write("-notimezeroasrtmsg" + os.linesep)
    write_file.write("-nbasync" + os.linesep)
    write_file.write("-nokey" + os.linesep)
    write_file.write("-licqueue" + os.linesep)
    write_file.write("-uvm" + os.linesep)
    write_file.write("-sv" + os.linesep)
    write_file.write("-forceelab" + os.linesep)
    #write_file.write("-uvm_opt" + os.linesep)

    if (args.uvm_verbosity == None):
        write_file.write("+UVM_VERBOSITY=" + "UVM_NONE" + os.linesep)
    else:
        write_file.write("+UVM_VERBOSITY=" + str(args.uvm_verbosity) + os.linesep)
    write_file.write("+UVM_USE_OVM_RUN_SEMANTIC" + os.linesep)
    if (args.uvm_timeout == None):
        write_file.write("+UVM_TIMEOUT=" + "4ms" + os.linesep)
    else:
        write_file.write("+UVM_TIMEOUT=" + str(args.uvm_timeout) + os.linesep)
    if (args.uvm_timeout == None):
        write_file.write("-svseed " + "25" + os.linesep)
    else:
        write_file.write("-svseed " + str(args.svseed) + os.linesep)
    write_file.write("-input $ARG_DIR/$testcase/run.tcl" + os.linesep)
    write_file.write("-l $LOG_DIR/$testcase/run.log" + os.linesep)

    write_file.write("-vlogext .udp" + os.linesep)
    write_file.write("-vlogext .vh" + os.linesep)
    write_file.write("-vlogext .vm" + os.linesep)
    write_file.write("-vlogext .vmp" + os.linesep)
    write_file.write("-vlogext .ncvp" + os.linesep)
    write_file.write("-nowarn DLCPTH" + os.linesep)
    write_file.write("-nowarn DLNCML" + os.linesep)
    write_file.write("-nowarn CUSRCH" + os.linesep)
    write_file.write("-nowarn RTSDAD" + os.linesep)
    write_file.write("-define RTL_SIM" + os.linesep)
    write_file.write("-define READSM" + os.linesep)
    write_file.write("-define TARGET_RENESAS" + os.linesep)

    if (args.fast_func == True):
        write_file.write("-define FAST_FUNC" + os.linesep)


    write_file.close()
    #print(args.accumulate(args.DEFINE))

# Steps to perform
# 1. Prepare directories
# 2. Declare and initialize internal variables and file names

prepare_cdslib()
create_seq_lib()
parse_command_line()
