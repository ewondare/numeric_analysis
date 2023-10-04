% Romberg integration

clear
f = @(x) sin(x);
a = 0;
b = pi;
h = input('Enter step size: ');
k = input('k for h/2^k: ');
m = (b-a)/h;

T = zeros(k+1,k+1);
% Compute T_0i (i = 0 to k) --- Substitute in T(i+1,1)
j = 0;
for i = 0:k 
    T(i+1,j+1) = f(a);
    for t = 1:m-1
        T(i+1,j+1) = T(i+1,j+1) + 2*f(a+t*h);
    end
    T(i+1,j+1) = T(i+1,j+1) + f(b);
    T(i+1,j+1) = h/2*T(i+1,j+1);
    
    h = h/2;
    m = 2*m;
end

% Compute T_ji (j= 1 to k, i = 0 to k-j) --- Substitute in T(i+1,j+1)
for j = 1:k
    for i = 0:k-j
        T(i+1,j+1) = ((4^j)*T(i+2,j)-T(i+1,j))/(4^j-1);
    end
end

ExSol = @(x) -cos(x);
Ex = ExSol(b)-ExSol(a);
Err = abs(Ex-T(1,k+1));
fprintf('T_%d0 = %.6f,  Error = %.4e \n', k, T(1,k+1), Err);







