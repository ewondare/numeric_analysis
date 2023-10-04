% Simpson's Rule

clear
f = @(x) 1./(1+x.^2);
a = 0;
b = 2;
n = input('Enter n (an even number): ');
h = (b-a)/n;
x = a:h:b;
m = length(x); %The number of points: n+1
S = f(x(1));
for i = 1:(m-3)/2
    S = S + 4*f(x(2*i)) + 2*f(x(2*i+1));
end
S = S + 4 * f(x(m-1))+ f(x(m));
S = h/3*S;
fprintf('S(h) = %.6f \n',S);

% Exact solution 
F = @(x) atan(x);
I = F(b)-F(a);

fprintf('Error = %.4e \n', abs(S-I));


