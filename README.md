# AutoCell
AutoCell是基于本人毕业设计的开源项目，致力于打造一个自动化的三维细胞培养系统。本项目主要是开发了一个远程可操控的网络系统，用于远程控制细胞培养系统的各个部分：荧光成像系统、位移台控制系统、环境监测系统、培养及监视任务管理系统和实验人员管理系统等。本项目前端的开发语言为TypeScript, 开发框架为Vue, 使用了element-ui; 后端部分的开发语言为Python, 使用了Flask作为web框架, 数据库使用了MySQL。硬件部分的控制核心为一个树莓派4B, 位移台和整体架构使用了定制铝型材加工搭建而成，使用了MKS作为步进电机的控制核心；自行搭建了一个简易的、低成本的小型荧光成像系统，使用470nm的LED作为光源，使用液体镜头作为对焦系统，可以清晰地对520nm的绿色荧光进行成像；系统还具有自动切换试剂的功能，气压源为一小型气泵，气压控制采用比例阀控制大小，电磁阀控制开关的机制，通过定制任务，可以完成不同试剂的切换工作。
## Build
You should open the 'web_ui' and run `npm i`, then run `webpack` to finish build the Ui for client.

You should open the 'App' and run `pip install -r requirements.txt`, then run `python main.py` for run Server.

You should open the '/APP/db/index.py' to check the MySQL connection




