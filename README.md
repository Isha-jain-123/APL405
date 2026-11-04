# APL405: Machine Learning in Mechanics

My lab assignments for APL405 (Machine Learning in Mechanics) at IIT Delhi, done in early 2022. The labs start from basic regression and build up to neural networks and physics-informed neural networks (PINNs), with most problems taken from solid mechanics.

Everything is written in Python. Labs 1 to 4 use NumPy, pandas, SciPy and Matplotlib, Lab 5 is a neural network written from scratch in NumPy, and Lab 6 uses PyTorch.

## Labs

| Lab | Topic | What's in it |
|-----|-------|--------------|
| [Lab 1](Lab1-Mohr's%20Circle) | Mohr's Circle | Finds the principal stresses of a 3×3 stress tensor from its eigenvalues and plots the 3D Mohr's circles. |
| [Lab 2](Lab2-Regression) | Regression | Q1: fits a nonlinear model `y = w0 + w1·x²` to `prob1data.txt` with gradient descent. Q2: multivariate linear regression for house prices (`prob2data.csv`) using bedrooms, bathrooms, living area, floors and year built, with feature normalisation. |
| [Lab 3](Lab3-Logistic%20Regression) | Logistic Regression | Cleans a weather dataset and trains a regularised logistic regression model to predict whether it will rain tomorrow. |
| [Lab 4](Lab4-Multiclass%20Classification) | Multiclass Classification | One-vs-all logistic regression on Fashion-MNIST, with a helper to display sample images and a test accuracy check. |
| [Lab 5](Lab5-Neural%20Networks) | Neural Networks | A feedforward network on Fashion-MNIST, written from scratch with sigmoid activations, comparing one and two hidden layers (25 units each). |
| [Lab 6](Lab6-PINNs) | Physics-Informed Neural Networks | PINNs in PyTorch for a 1D bar under distributed load (Q1) and an Euler-Bernoulli beam with displacement and slope boundary conditions (Q2). The loss combines the residual of the governing differential equation with the boundary condition errors, and the predictions are compared with the analytical solutions. |

Each lab folder contains the code (`.py` scripts or Jupyter notebooks), and most of them also include a PDF with the figures I submitted.

## Running the code

```bash
git clone https://github.com/Isha-jain-123/APL405.git
cd APL405
pip install numpy pandas scipy matplotlib torch jupyter
```

- Labs 3 and 4 download their datasets from the course repository, so you need an internet connection.
- Lab 5 expects `fashion-mnist_train.csv` and `fashion-mnist_test.csv` in the same folder as the notebook.
- For Lab 6, run the notebooks from inside `Lab6-PINNs/` so that `utilities.py` and the model files can be imported.

Some scripts were exported from Google Colab, so a few lines (file uploads, `%matplotlib inline`) are commented out.
