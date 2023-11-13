# Activation Functions

Glossary
: 1. [Activation Function 激活函数]{#acti}
  2. [Differential 微分]{#diff}
  3. [Derivative 导数]{#deri}
  4. [Gradient 梯度]{#grad}

Activation Functions
: [Activation functions](#acti) decide whether a neuron should be activated
  or not by calculating the weighted sum and further adding bias to it. \
  They are [differential](#diff) operators for transforming input
  signals to outputs, while most of them add non-linearity.

## ReLU Function

ReLU provides a very simple nonlinear transformation. Given an element,
the function is defined as the maximum of that element and 0. \
The ReLU function retains only positive elements and discards all negative
elements by setting the corresponding activations to 0. \
When the input is negative, the [derivative](#deri) of the
is 0, and when the input is positive, the derivative of the ReLU function
is 1. \
It mitigated the well-documented problem of vanishing
{ref}`gradients <grad>`.

:::{math}
\operatorname{ReLU}(x) = \max(x, 0)
:::

## Sigmoid Function

The sigmoid function transforms those inputs whose values lie in the
domain {math}`\mathbb{R}`, to outputs that lie on the interval (0, 1).

:::{math}
\operatorname{sigmoid}(x) = \frac{1}{1 + \exp(-x)}
:::
