
myCone(0,0,0)

fimplicit3(@myCone, [-2 2 -2 2 -2 2], 'EdgeColor', 'none', 'FaceAlpha', 0.6)
xlabel('X'); ylabel('Y'); zlabel('Z');
xlim([-2, 2]);
ylim([-2, 2]);
zlim([-2, 2]);


function f = test(x,y,z)
f = x.^2 + y.^2 - z.^2 - 1;
end



function f = myCone(x, y, z)
x0 = 0;
y0 = 0;
z0 = 0;
theta = 0;
phi = 0;
alpha = 20;
a = ((x - x0)*cosd(phi) - (y - y0)*sind(phi)).^2;
b = (((x - x0)*sind(phi) + (y - y0)*cosd(phi))*cosd(theta) - (z - z0)*sind(theta)).^2;
c = (((x - x0)*sind(phi) + (y - y0)*cosd(phi))*sind(theta) + (z - z0)*cosd(theta)).^2;
f = c*tand(alpha/2) - b - a;
end
%% 


%fimplicit3(c, [-2 2 -2 2 -2 2], 'EdgeColor', 'none', 'FaceAlpha', 0.6)
%xlabel('X'); ylabel('Y'); zlabel('Z');