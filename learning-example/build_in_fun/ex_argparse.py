import argparse
parser = argparse.ArgumentParser()
# 位置参数 
parser.add_argument('ps1')
# 变量参数
parser.add_argument('-p','--ps2',help='input value2')
# 默认填写值
parser.add_argument('-v','--verbose',help='input value3',action='store_true')
# 类型
parser.add_argument('-x','--xtype',type=int)
# 可选值
parser.add_argument('-y','--choice',choices=[0,1,2],type=int)
# 必要参数
parser.add_argument('-f','--file',required=True)
# 互斥参数
group = parser.add_mutually_exclusive_group()
group.add_argument('-v','--verbose',action='store_true')
group.add_argument('-q','--quiet',action='store_true')
# 参数默认值
parser.add_argument('-v','--verbose',default=1)
args = parser.parse_args()
args.verbose
args.ps1