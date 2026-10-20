require('./get_cb')
function generateRealTrace(startX = 184, distance = 200, totalFrames = 100) {
    let trace = [];
    let currentTime = Math.floor(Math.random() * 10) + 1; // 初始时间（比如 4）

    for (let i = 0; i < totalFrames; i++) {
        // 1. 计算当前进度 (0 到 1)
        let progress = i / (totalFrames - 1);

        // 2. 模拟人类滑动曲线（先加速，后减速）
        // 这里使用三次贝塞尔曲线或者简单的缓动函数
        let easeOutProgress = 1 - Math.pow(1 - progress, 3);

        // 3. 计算当前理论 X 坐标
        let currentX = startX + distance * easeOutProgress;

        // 4. 加入人类手抖造成的随机误差 (增量不会绝对均匀)
        let jitter = (Math.random() - 0.5) * 5; // -2.5 到 +2.5 像素的抖动

        // 5. 拼接成真实格式：[时间, Y轴, X轴, 状态]
        // 注意：这里的 X 很多时候风控要求是整数，用 Math.round 取整
        trace.push([
            currentTime,
            0,
            Math.round(currentX + jitter),
            1
        ]);

        // 6. 时间递增 (模拟真实移动时的帧率，一般在 8ms - 20ms 之间)
        currentTime += Math.floor(Math.random() * 12) + 4;
    }

    // 确保最后一个点是绝对精准的终点
    trace.push([currentTime, 0, startX + distance, 1]);

    return trace;
}
function get_trace_data(trace, token) {
    var trace_list = []; // 准备一个空数组存结果
    for (var i of trace) { // 遍历传入的 trace 数组（比如鼠标轨迹、时间戳等）
        // 对于 trace 中的每一个元素 i，将其转为字符串，连同 token 一起传入加密函数
        // 注意：图片中的 _0x3ca67b: 是调试工具（如VSCode/Chrome）提示的参数名，实际运行代码没有这个
        var new_trace_data = window._0x3855dc(token, i + '');
        trace_list.push(new_trace_data); // 将加密后的结果推入数组
    }
    return trace_list; // 返回加密后的轨迹数组
}

function get_params_data(trace,token,slide)
{
    var trace_data = get_trace_data(trace, token)
    var _0x4a4a62 = window._0x148293["sample"](trace_data, 50)
    var _0x15278a = window._0x3ebd00(window._0x3855dc(token, slide/ 300 *100+ ''))
    var _0x4d98f2 = window._0x6e07ce(window._0x148293["unique2DArray"](trace,2))
    return JSON["stringify"]
    (
        {
            'd': window._0x3ebd00(_0x4a4a62['join'](':')),
            'm': '',
            'p': _0x15278a,
            'f': window._0x3ebd00(window._0x3855dc(token, _0x4d98f2['join'](','))),
            'ext': window._0x3ebd00(window._0x3855dc(token, 1 + ',' +trace_data['length']))
        }
    )
}
function get_check_params(token, slide) {
    var trace = generateRealTrace(184, slide);
    return get_params_data(trace, token, slide);
}
window.get_check_params = get_check_params;

function get_callback() {
    return "__JSONP" + ("_" + Math.random().toString(36).slice(2, 9)) + ("_" + 1);
}
window.get_callback = get_callback;