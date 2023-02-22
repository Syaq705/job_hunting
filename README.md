# 2x2_cube
<br>
<br>
2x2のルービックキューブが遊べるプログラムです。<br>
自動で混ぜる機能を搭載しています。<br>
ルービックキューブに関しては下記のURLをご参照ください。<br>
<br>

#### 株式会社メガハウス
https://www.megahouse.co.jp/megatoy/products/item/3764/
<br>
<br>
<br>

## フォルダ構成
<br>
cube<br>
　2x2_cube.py　：　メインファイル<br>
　rotate.py　　：　回転用モジュール<br>
<br>
<br>

## 開発環境

| 環境 | ソフトウェア名 |
| ------------- | ------------- |
| OS  | Windows10  |
| 言語  | Python  |
| プラットフォーム  | Anaconda  |
| 外部ライブラリ  | NumPy  |
<br>

## 機能
<br>
・自動シャッフル<br>
・持ち替え<br>
・一面回転<br>
<br>
<br>

## 作成背景
<br>
前職でWebスクレイピングの際にPythonに出会いほぼ独学で習得したため、<br>
現在Pythonの職業訓練校に通い不足していた知識を補っております。<br>
<br>
職業訓練校の最後には簡単な作品提出という課題があるため、<br>
演習の残り時間や休憩時間などを利用し事前学習として本作品を作成しました。<br>
<br>
題材選定理由は作品提出にあたり個人的に楽しさを取り入れたいという点から単純な発想としてゲームが思いつき、<br>
トランプやテトリスといった2次元的な物よりも表現が難しい3次元的な物に挑戦したいと考え、<br>
趣味としてもルービックキューブ系パズルを自力で解くことに夢中になっていることから<br>
3次元的に最もシンプルで表現がしやすい2x2x2のルービックキューブを題材に選定しました。<br>


#### ポイント

2x2x2の立体的なものを画面上に表現するため4x4x4の枠組みを用意し、<br>
表現に必要ない部分は空白とすることで立体的に再現しました。<br>

特に側面の回転に関してが通常のリストなどでは難しく、<br>
１つずつ数値の書換えでも実装は可能ですが、<br>
コーディングミスにも繋がるためNumPyで多次元配列を扱い、<br>
rot90関数で指定平面の回転を簡単に行いました。<br>
<br>
また文字列だけの場合視認性が非常に悪かったため、<br>
計算用とは別にテキストとして文字の背景に色を付けました。<br>

