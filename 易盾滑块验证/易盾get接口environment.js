// 补环境脚本
function get_enviroment(proxy_array) {
    for (let i = 0; i < proxy_array.length; i++) {
        const prop = proxy_array[i]; // 获取属性名，如 'window' 或 'document'

        // 定义拦截器
        const handler = {
            get: function(target, property, receiver) {
                // 使用反引号或 + 号拼接变量
                console.log(`方法: get 对象: ${prop} 属性: ${String(property)} 属性类型: ${typeof property} 属性值类型: ${typeof target[property]}`);
                return target[property];
            },
            set: function(target, property, value, receiver){
                console.log(`方法: set 对象: ${prop} 属性: ${String(property)} 属性类型: ${typeof property} 属性值类型: ${typeof target[property]}`);
                return Reflect.set(...arguments);
            }
        };

        try {
            // 尝试获取全局变量 (Node中相当于 window.xxx)
            let obj = global[prop];
            // 如果变量不存在或者不是对象，抛出异常进入 catch
            if (!obj || typeof obj !== 'object') {
                throw new Error('Not exist');
            }
            // 代理已经存在的对象
            global[prop] = new Proxy(obj, handler);
        } catch (e) {
            // 如果不存在，创建一个空对象并代理
            console.log(`[!] 未找到 ${prop}，已自动创建空对象并代理`);
            global[prop] = {};
            global[prop] = new Proxy(global[prop], handler);
        }
    }
}

// 必须先声明 window 挂载到 global 上
global.window = global; // 或者 global.window = {}
div={
    className:'div',

    addEventListener:function (){},

    getAttribute:function (attr){
        console.log("div getAttribute->",attr)
    }
}

document={
    body:{},

    getElementById:function (ele_id){
        console.log("document getElementById->",ele_id)
    },

    createElement:function (ele_name){
        console.log("document createElement->",ele_name)
        if (ele_name=='div'){
            return div
        }
    }
}

navigator={
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

location={
    "ancestorOrigins": {},
    "href": "https://dun.163.com/trial/sense",
    "origin": "https://dun.163.com",
    "protocol": "https:",
    "host": "dun.163.com",
    "hostname": "dun.163.com",
    "port": "",
    "pathname": "/trial/sense",
    "search": "",
    "hash": ""
}
setTimeout=function () {}
setInterval=function () {}

// 需要代理的全局对象数组
const proxy_array = ['window', 'document','div','navigator','location'];

get_enviroment(proxy_array);