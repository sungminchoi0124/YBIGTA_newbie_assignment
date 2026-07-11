#!/bin/bash

# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if [ ! -d "$HOME/miniconda" ]; then
    echo "[INFO] Conda가 존재하지 않아 Miniconda를 설치합니다."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda
    rm miniconda.sh
fi

export PATH="$HOME/miniconda/bin:$PATH"

# Conda 환셩 생성 및 활성화
## TODO
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main || true
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r || true
conda create -n myenv python=3.10 -y
eval "$(conda shell.bash hook)"
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
conda install mypy -y

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    filename="${file%.py}"
    prob_num="${filename#*_}"
    python "$file" < "../input/${prob_num}_input" > "../output/${prob_num}_output"
done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy . > ../mypy_log.txt || true

# conda.yml 파일 생성
## TODO
conda env export > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate