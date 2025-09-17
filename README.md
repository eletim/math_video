
# install

```sh
sudo apt update
# 画面合成に必要
sudo apt install -y ffmpeg
# Cairo/Pango（pycairo関連で必要になることがあります）
sudo apt install -y libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0
# もしビルドで詰まったら dev 版も
# sudo apt install -y libcairo2-dev libpango1.0-dev pkg-config
# LaTeX（MathTexを使うなら入れておく）
sudo apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended dvipng
```

```
cd math_video
python3 -m venv .venv
source .venv/bin/activate

pip install -U pip wheel setuptools
pip install manim
```


# play

```sh
python -m manim -pql math_anim.py SolveByFactoring    # 低画質プレビュー
# 高画質
python -m manim -pqh math_anim.py SolveByFactoring
# GIF が欲しい場合
python -m manim -pqh --format=gif math_anim.py SolveByFactoring
```
