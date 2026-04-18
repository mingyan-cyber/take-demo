import matplotlib.pyplot as plt
import numpy as np


def plot_takebeat_dashboard(
    user_name: str,
    trimp: int,
    strain_7d: int,
    tolerance_28d: int,
    training_level: str,
    training_status: str,
    output_file: str = "takebeat_dashboard.png",
    show_plot: bool = True,
) -> None:
    """绘制 TakeBeat 训练负荷看板并保存为 PNG。"""
    # 解决中文乱码
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    metrics = ["单次训练负荷\nTRIMP", "最近7天训练压力\nStrain", "最近28天训练耐受力\nTolerance"]
    values = [trimp, strain_7d, tolerance_28d]
    colors = ["#2F80ED", "#F2994A", "#27AE60"]

    fig = plt.figure(figsize=(12, 7), dpi=140, facecolor="#F7F9FC")
    gs = fig.add_gridspec(6, 6, left=0.06, right=0.95, top=0.9, bottom=0.08, hspace=0.6)

    ax_title = fig.add_subplot(gs[0, :])
    ax_title.axis("off")
    ax_title.text(0.0, 0.8, "TakeBeat 训练负荷看板", fontsize=26, fontweight="bold", color="#1F2D3D")
    ax_title.text(0.0, 0.15, f"用户：{user_name}", fontsize=16, color="#3C4858")

    ax_bar = fig.add_subplot(gs[1:5, :4])
    ax_bar.set_facecolor("white")

    y_pos = np.arange(len(metrics))
    bars = ax_bar.barh(y_pos, values, color=colors, height=0.5, edgecolor="none")

    ax_bar.set_yticks(y_pos)
    ax_bar.set_yticklabels(metrics, fontsize=12)
    ax_bar.set_xlim(0, 100)
    ax_bar.set_xlabel("负荷指数", fontsize=12)
    ax_bar.grid(axis="x", linestyle="--", alpha=0.25)
    ax_bar.invert_yaxis()
    ax_bar.set_title("核心训练指标", fontsize=16, fontweight="bold", pad=14)

    for bar, value in zip(bars, values):
        ax_bar.text(
            value + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{value}",
            va="center",
            fontsize=12,
            color="#1F2D3D",
            fontweight="bold",
        )

    ax_info = fig.add_subplot(gs[1:5, 4:])
    ax_info.set_facecolor("white")
    ax_info.set_xticks([])
    ax_info.set_yticks([])
    for spine in ax_info.spines.values():
        spine.set_visible(False)

    ax_info.text(0.06, 0.82, "单次训练等级", fontsize=13, color="#6B778C")
    ax_info.text(0.06, 0.68, training_level, fontsize=26, color="#2F80ED", fontweight="bold")

    ax_info.text(0.06, 0.42, "当前训练状态", fontsize=13, color="#6B778C")
    ax_info.text(0.06, 0.27, training_status, fontsize=24, color="#27AE60", fontweight="bold")

    score = round((trimp * 0.45 + strain_7d * 0.35 + tolerance_28d * 0.20), 1)
    ax_info.text(0.06, 0.08, f"综合负荷评分：{score}", fontsize=12, color="#3C4858")

    fig.text(0.06, 0.02, "注：本图用于训练负荷趋势展示，建议结合恢复指标综合评估。", fontsize=10, color="#7A869A")

    plt.savefig(output_file, dpi=180, bbox_inches="tight")
    print(f"已保存 PNG 文件：{output_file}")

    if show_plot:
        plt.show()

    plt.close(fig)


if __name__ == "__main__":
    # 样例数据
    plot_takebeat_dashboard(
        user_name="用户A",
        trimp=85,
        strain_7d=70,
        tolerance_28d=65,
        training_level="中等",
        training_status="高效",
        output_file="takebeat_dashboard.png",
        show_plot=True,
    )
