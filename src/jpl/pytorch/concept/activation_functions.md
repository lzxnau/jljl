# Activation Functions

Activation Functions
: Activation functions(激活函数)decide whether a neuron should be activated
  or not by calculating the weighted sum and further adding bias to it. \
  They are differential operators(微分操作符D)for transforming input signals
  to outputs, while most of them add nonlinearity.

## ReLU Function

ReLU provides a very simple nonlinear transformation. Given an element,
the function is defined as the maximum of that element and 0. \
The ReLU function retains only positive elements and discards all negative
elements by setting the corresponding activations to 0. \
When the input is negative, the derivative(导数) of the ReLU function is 0,
and when the input is positive, the derivative of the ReLU function is 1. \
It mitigated the well-documented problem of vanishing gradients(梯度).

:::{math}
\operatorname{ReLU}(x) = \max(x, 0)
:::

## Sigmoid Function

The sigmoid function transforms those inputs whose values lie in the
domain {math}`\mathbb{R}`, to outputs that lie on the interval (0, 1).

:::{math}
\operatorname{sigmoid}(x) = \frac{1}{1 + \exp(-x)}
:::


