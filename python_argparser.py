import argparse
import os

def go_to_root_dir(root_dir_name):
    print(root_dir_name)
    pwd = os.getcwd()
    print("Present working dir: " + pwd)
    head_tail = os.path.split(pwd)

    # print head and tail
    # of the specified path
    print("Head of '% s:'" % pwd, head_tail[0])
    print("Tail of '% s:'" % pwd, head_tail[1], "\n")

    temp = '/'+root_dir_name
    print(temp)
    while (head_tail[0] != temp):
        pwd = head_tail[0]
        print("Present working dir: " + pwd)
        head_tail = os.path.split(pwd)

        # print head and tail
        # of the specified path
        print("Head of '% s:'" % pwd, head_tail[0])
        print("Tail of '% s:'" % pwd, head_tail[1], "\n")

    os.chdir(head_tail[0])
    pwd = os.getcwd()
    print("Present working dir: " + pwd)


if __name__ == "__main__":
    print("OS Name: " + os.name)
    parser = argparse.ArgumentParser("series_c_fpga_builder.py")
    parser.add_argument('--HIA_FPGA_FLAVOR',
        choices= ['GHIA', 'IHIA', 'OHIA_LV2', 'F_IHIA', 'F_OHIA_LV2', 'ALL_UNFAULTED', 'ALL_FAULTED', 'ALL'],
        help='Usage: --HIA_FPGA_FLAVOR [GHIA | IHIA | OHIA_LV2 | F_IHIA | F_OHIA_LV2 | ALL_UNFAULTED | ALL_FAULTED | ALL]')

    parser.add_argument('--IFIA_FPGA_FLAVOR',
        help='Usage: --IFIA_FPGA_FLAVOR [AIFIA | DIFIA | F_AIFIA | F_DIFIA | \
                ALL_UNFAULTED | ALL_FAULTED | ALL]',
        choices= ['AIFIA', 'DIFIA', 'F_AIFIA', 'F_DIFIA' \
                'ALL_UNFAULTED', 'ALL_FAULTED', 'ALL'] )
    parser.add_argument('--FPU', help='Usage: --FPU [FPU]', choices=['FPU'])

args = parser.parse_args()
#print(args)
print("Argument HIA_FPGA_FLAVOR value is: " + str(args.HIA_FPGA_FLAVOR))
if (str(args.HIA_FPGA_FLAVOR) == "GHIA"):
    print("Build GHIA")
    #os.system("quartus_sh -t ../../../proc/scripts/synth/GHIA_quartus_run.tcl")

if (str(args.HIA_FPGA_FLAVOR) == "IHIA"):
    print("Build IHIA")

if (str(args.HIA_FPGA_FLAVOR) == "OHIA_LV2"):
    print("Build OHIA_LV2")

if (str(args.HIA_FPGA_FLAVOR) == "F_IHIA"):
    print("Build Faulted IHIA")

if (str(args.HIA_FPGA_FLAVOR) == "F_OHIA_LV2"):
    print("Build Faulted OHIA_LV2")

if (str(args.HIA_FPGA_FLAVOR) == "IHIA"):
    print("Build IHIA")

if (str(args.HIA_FPGA_FLAVOR) == "ALL_UNFAULTED"):
    print("Build GHIA")
    print("Build IHIA")
    print("Build OHIA_LV2")

if (str(args.HIA_FPGA_FLAVOR) == "ALL_FAULTED"):
    print("Build F_IHIA")
    print("Build F_OHIA_LV2")

if (str(args.HIA_FPGA_FLAVOR) == "ALL"):
    print("Build GHIA")
    print("Build IHIA")
    print("Build OHIA")
    print("Build F_IHIA")
    print("Build F_OHIA_LV2")

go_to_root_dir("home")

pwd = os.getcwd()
temp = pwd+'/bulbul/Downloads'
os.chdir(temp)
pwd = os.getcwd()
print("Present working dir: " + pwd)
files = os.listdir(pwd)
for f in files:
    print(f)
