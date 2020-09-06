import os
import argparse

parser = argparse.ArgumentParser("text_to_function.py")
parser.add_argument('--INPUT_FILE',
    help='Usage: --INPUT_FILE <input file path>')
parser.add_argument('--OUTPUT_FILE',
    help='Usage: --OUTPUT_FILE <output file path>')

args = parser.parse_args()
#print(args)
print("Argument INPUT_FILE value is: " + str(args.INPUT_FILE))
if (str(args.INPUT_FILE) == "None"):
    print("ERROR: No input file specified!")
    quit()

print("Argument OUTPUT_FILE value is: " + str(args.OUTPUT_FILE))
if (str(args.OUTPUT_FILE) == "None"):
    print("ERROR: No output file specified!")
    quit()

read_file  = open(args.INPUT_FILE, mode='r')
write_file = open(args.OUTPUT_FILE, mode='w')

print("Creating a Python function from a given TCL file.")
print("When the function will be called, it will re-create the TCL file.")
print("The IDEA is, user will give a TCL file.")
print("Then This program will create a Python function from the TCL file.")
print("Later a Python program will use the Python function in FPGA build script to re-create the TCL file.")
print("After first iteration, we need to maintain only the Python function for any project settings related modifications.")
write_file.write("import os \n\n")
write_line = "def create_tcl():" + os.linesep
write_file.write(write_line)
write_line = "\twrite_f = open(\"build_fpga.tcl\", mode=\'w\')" + os.linesep
write_file.write(write_line)
write_file.write("\t" + r'write_f.write("load_package flow")' + os.linesep)
for line in read_file:
    print(line.rstrip())
    str_split = (line.rstrip()).split(" ", 8)

    # Replace " with \"
    write_line = line.rstrip()
    write_line = write_line.replace("\"", "\\\"")

    # Extract Top level entity name from QSF file
    for i in range(len(str_split)):
        if (str_split[i] == "TOP_LEVEL_ENTITY"):
            top_level_entity = str_split[i+1]
            print("Top = " + top_level_entity)

    write_line = r'write_f.write("' + write_line + r'" + os.linesep)'
    write_file.write("\t" + write_line + os.linesep)

write_file.write("\t" + r'write_f.write("\n\n" + os.linesep)' + os.linesep)
# Altera build process starts
write_file.write("\t" + r'write_f.write("# Altera build process starts" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("# compile the project" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("# execute_flow -compile" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("# Compile using a set of executables" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("# execute_module -tool map" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool map} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write(" puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: Analysis and Synthesis failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: Analysis and Synthesis was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool fit" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool fit} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: Fit failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: Fit was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool asm" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool asm} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: Bitmap Generation failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: Bitmap Generation was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool sta" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool sta} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: Static timing analysis failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: Static timing analysis was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool eda" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool eda -args \"--simulation=on --map_illegal_characters --functional --tool=ncsim --format=vhdl --gen_script=rtl_and_gate_level --glitch_filtering=on\"} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: VHDL Timing netlist generation failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: VHDL Timing netlist generation was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool eda" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool eda -args \"--simulation=on --map_illegal_characters --functional --tool=ncsim --format=verilog --gen_script=rtl_and_gate_level --glitch_filtering=on\"} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: Verilog Timing netlist generation failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: Verilog Timing netlist generation was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool pow" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("if {[catch {execute_module -tool pow -args \"--default_input_io_toggle_rate=25% --default_toggle_rate=25% \"} result]} {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: Power estimation report generation failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: Power estimation report generation was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool cdb" + os.linesep)' + os.linesep)
write_line = "write_f.write(" + "\"if {[catch {execute_module -tool cdb -args --vqm=" + top_level_entity + ".vqm} result]} {\"" + " + os.linesep)"
write_file.write("\t" + write_line + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: VQM writing failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: VQM writing was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool cpf" + os.linesep)' + os.linesep)
write_line = "write_f.write(" + "\"if {[catch {execute_module -tool cpf -args \\\"-c output_files/" + top_level_entity + ".sof output_files/" + top_level_entity + ".hexout --option ../../../proc/scripts/synth/quartus_cpf_option_file\\\"} result]} {\" + os.linesep)"
write_file.write("\t" + write_line + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: HEXOUT file writing failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: HEXOUT file writing was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#execute_module -tool cpf" + os.linesep)' + os.linesep)
write_line = "write_f.write(" + "\"if {[catch {execute_module -tool cpf -args \\\"-c output_files/" + top_level_entity + ".sof output_files/" + top_level_entity + ".rbf --option ../../../proc/scripts/synth/quartus_cpf_option_file\\\"} result]} {\" + os.linesep)"
write_file.write("\t" + write_line + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nResult: $result\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"ERROR: RBF file writing failed. See the report file.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("} else {" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("	puts \"\\nINFO: RBF file writing was successful.\\n\"" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("}" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("#report_rtl_pin_summary" + os.linesep)' + os.linesep)
write_file.write("\t" + r'write_f.write("project_close" + os.linesep)' + os.linesep)

write_line = "\t" + r'write_f.close()' + os.linesep
write_file.write(write_line)

write_file.write("create_tcl()" + os.linesep)

# Execute bitmap gen
write_file.write("#os.system(quartus_sh -t build_fpga.tcl)" + os.linesep)

read_file.close()
write_file.close()
