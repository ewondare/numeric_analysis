% Trapezoidal Rule

clear
f = @(x) log(x);
a = 1;
b = 2;
h = input('Enter step size: ');

x = a:h:b;
m = length(x); %The number of points: n+1
T = f(x(1));
for i = 2:m-1
    T = T + 2*f(x(i));
end
T = T + f(x(m));
T = h/2*T;
fprintf('T(h) = %.6f \n',T);

% Exact solution 
F = @(x) x*log(x)-x;
I = F(b)-F(a);

fprintf('Error = %.6f \n', abs(T-I));


