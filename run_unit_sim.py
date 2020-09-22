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
    parser.add_argument('--DEFINE', nargs='+',
        help='Usage: --DEFINE < define(s) to pass to test bench>')
    parser.add_argument('--sixty_four', action='store_true',
        help='To enable XRUN run on 64 bit mode')

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

if($use_timing_check == 0){  
     print {$ARGFILE_FH} "-notimingchecks\n";
  }
  if($use_specify == 0){
     print {$ARGFILE_FH} "-nospecify\n";
  }
  print {$ARGFILE_FH} "-no_tchk_msg\n";
 # print {$ARGFILE_FH} "-define RTL_SIM\n";
  print {$ARGFILE_FH} "-notimezeroasrtmsg\n";
  print {$ARGFILE_FH} "-nbasync\n";
  print {$ARGFILE_FH} "-nokey\n";
  print {$ARGFILE_FH} "-licqueue\n";
  print {$ARGFILE_FH} "-uvm\n";
  print {$ARGFILE_FH} "-sv\n";
  print {$ARGFILE_FH} "-forceelab\n";
  if ($ovl_on) {
    print {$ARGFILE_FH} "-ovl SVA +sv\n";
  }
  print {$ARGFILE_FH} "$uvm_opt\n";
  print {$ARGFILE_FH} "+UVM_TESTNAME=$test_name\n";
  print {$ARGFILE_FH} "+UVM_VERBOSITY=$uvm_verbosity\n";
  print {$ARGFILE_FH} "+UVM_USE_OVM_RUN_SEMANTIC\n";
  print {$ARGFILE_FH} "+UVM_TIMEOUT=$timeout,NO\n";
  print {$ARGFILE_FH} "-svseed $random_seed\n";
  print {$ARGFILE_FH} "-top $TB_TOP_FILE\n";
  print {$ARGFILE_FH} "-input $ARG_DIR/$testcase/run.tcl\n";
  print {$ARGFILE_FH} "-l $LOG_DIR/$testcase/run.log\n";
  print {$ARGFILE_FH} "-vlogext .udp\n";
  print {$ARGFILE_FH} "-vlogext .vh\n";
  print {$ARGFILE_FH} "-vlogext .vm\n";
  print {$ARGFILE_FH} "-vlogext .vmp\n";
  print {$ARGFILE_FH} "-vlogext .ncvp\n";
  print {$ARGFILE_FH} "-nowarn DLCPTH\n";
  print {$ARGFILE_FH} "-nowarn DLNCML\n";
  print {$ARGFILE_FH} "-nowarn CUSRCH\n";
  print {$ARGFILE_FH} "-nowarn RTSDAD\n";
  print {$ARGFILE_FH} "-define RTL_SIM\n";
  print {$ARGFILE_FH} "-define READSM\n";
  print {$ARGFILE_FH} "-define TARGET_RENESAS\n";
  if($no_fast_func == 0){
  print {$ARGFILE_FH} "-define FAST_FUNC\n";
 

    write_file.close()
    #print(args.accumulate(args.DEFINE))


prepare_cdslib()
create_seq_lib()
parse_command_line()
