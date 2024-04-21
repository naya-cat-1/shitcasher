!function(){
    console.log(`这是引入的包入口,导导你的，真导嘛`)
    }()
const IPCExplorer = require('ipc-explorer');

// 创建一个类来封装IPC相关操作
class ShitCasher {
    constructor() {
        this.ipc = new IPCExplorer();
        console.log('ShitCasher 初始化完成。');
    }

    // 用于发送数据的方法
    sendData(data) {
        this.ipc.send('channel1', data);
        console.log(`数据发送至channel1: ${data}`);
    }

    // 用于接收数据的方法
    receiveData() {
        this.ipc.on('channel1', (data) => {
            console.log(`从channel1接收到数据: ${data}`);
            return data;
        });
    }

    // 模拟一些业务逻辑
    performTask(taskDetails) {
        console.log(`执行任务: ${taskDetails}`);
        // 这里可以加入更复杂的业务逻辑
    }
}

// 导出ShitCasher类
module.exports = ShitCasher;

// 打印包加载信息
console.log('shitcasher 包已加载。');