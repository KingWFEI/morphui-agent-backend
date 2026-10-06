"""演示页面：由 /preview 直接返回，供前端「实时预览」面板的 iframe 加载。

页面会通过相对路径 fetch /api/health，用于直观验证「预览中的项目 ↔ 后端」的连通性。
"""

PREVIEW_HTML = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>MorphUI 预览沙箱</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    min-height: 100vh;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif;
    background:
      radial-gradient(1200px 500px at 80% -10%, rgba(217, 119, 87, 0.16), transparent 60%),
      linear-gradient(160deg, #1c1b19 0%, #262624 60%, #2a241f 100%);
    color: #f0eee6;
    padding: 32px;
  }
  header { display: flex; align-items: center; justify-content: space-between; }
  h1 { font-size: 20px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
  .mark { width: 12px; height: 12px; background: #d97757; border-radius: 3px; transform: rotate(45deg); display: inline-block; }
  #clock { font-variant-numeric: tabular-nums; color: #8f8d86; font-size: 13px; }
  .sub { margin-top: 10px; color: #8f8d86; font-size: 13px; line-height: 1.6; }
  .grid { margin-top: 26px; display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 14px; }
  .card { background: rgba(255, 255, 255, 0.045); border: 1px solid rgba(255, 255, 255, 0.09); border-radius: 14px; padding: 16px; }
  .card .k { font-size: 12px; color: #8f8d86; }
  .card .v { margin-top: 8px; font-size: 22px; font-weight: 600; }
  .card .v.ok { color: #5bbf6e; }
  .card .v.pulse { color: #d97757; }
  .bar { margin-top: 12px; height: 6px; border-radius: 4px; background: rgba(255, 255, 255, 0.08); overflow: hidden; }
  .bar i { display: block; height: 100%; border-radius: 4px; background: linear-gradient(90deg, #d97757, #e39a7f); animation: glow 2.4s ease infinite alternate; }
  @keyframes glow { from { filter: brightness(0.9); } to { filter: brightness(1.3); } }
  .api { margin-top: 24px; font-size: 13px; color: #bab7ae; background: rgba(255, 255, 255, 0.04); border: 1px dashed rgba(255, 255, 255, 0.14); border-radius: 12px; padding: 12px 14px; }
  .api b { color: #5bbf6e; font-weight: 600; }
  .api b.bad { color: #e2604f; }
</style>
</head>
<body>
  <header>
    <h1><span class="mark"></span>MorphUI 预览沙箱</h1>
    <span id="clock">--:--:--</span>
  </header>
  <p class="sub">本页面由 FastAPI 后端直接返回，用于验证前端「实时预览」区域。修改后端 app/demo_page.py 后刷新即可看到变化。</p>
  <div class="grid">
    <div class="card"><div class="k">构建状态</div><div class="v ok">● Running</div><div class="bar"><i style="width:72%"></i></div></div>
    <div class="card"><div class="k">组件渲染</div><div class="v pulse">128</div><div class="bar"><i style="width:58%"></i></div></div>
    <div class="card"><div class="k">接口延迟</div><div class="v" id="latency">-- ms</div><div class="bar"><i style="width:34%"></i></div></div>
  </div>
  <div class="api">后端心跳：<b id="api">检测中…</b></div>
  <script>
    const clock = document.getElementById('clock');
    const tick = () => { clock.textContent = new Date().toLocaleTimeString('zh-CN', { hour12: false }); };
    tick(); setInterval(tick, 1000);
    const t0 = performance.now();
    fetch('/api/health')
      .then((r) => r.json())
      .then((d) => {
        document.getElementById('latency').textContent = Math.max(1, Math.round(performance.now() - t0)) + ' ms';
        document.getElementById('api').textContent = d.service + ' · ' + d.status + ' · v' + d.version;
      })
      .catch(() => {
        const el = document.getElementById('api');
        el.textContent = '连接失败';
        el.className = 'bad';
      });
  </script>
</body>
</html>"""
