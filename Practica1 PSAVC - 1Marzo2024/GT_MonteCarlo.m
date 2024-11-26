%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% PSAVC - Practica de deteccion por Group Testing
%
% Codigo de Matlab a completar para los apartados 4 y 5 del trabajo de
% laboratorio
% NOTA: el codigo de matlab puede vectorizarse para hacerlo mas eficiente,
% no se ha hecho para facilitar la comprension.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% -----------  Parametros de la simulacion

m0   = 5;  % Modelo estadistico de la funcion de test basica
m1   = 10; % Modelo estadistico de la funcion de test basica
var0 = 1;  % Modelo estadistico de la funcion de test basica
var1 = 1.2;% Modelo estadistico de la funcion de test basica
p    = 0.1;% Probabilidad de individuo infectado
K    = 2;  % Tamaño de los grupos en el detector GT

gamma_clasico = ##completar## % Umbral de deteccion gamma en el detector clasico para P_FA<=0.005 y p=0.1
gamma_GT      = ##completar## % Umbral de deteccion gamma en el detector GT con K=2 para P_FA<=0.005 y p=0.1


N    = ##completar##; % Numero de individuos en la poblacion a simular (Poner un valor grande!)

    
%% -----------  Apartado 4.5: Resultados de MonteCarlo

%---- Generacion de los individuos con estados aleatorios con probabilidad p de estar infectados
%     Vector de tamaño 1 fila, N columnas con posicion i-esima de valor ...
%          ... 0 si el individuo i-esimo no esta infectado 
%          ... 1 el el individuo i-esimo si esta infectado
estado_individuos    = ##completar##;


%---- Simulacion del detector clasico: 
decision_clasico = ones(1,N); % Inicializacion de la variable decision_clasico 
                               % Esta variable guarda las decisiones tomadas por el
                               % detector clasico en un vector de 1 fila y N columnas. 
                               % El elemento i guarda la decision tomada sobre el i-esimo individuo

for indice_individuo=1:N
    y = realizacion_funcion_test (estado_individuos(indice_individuo),m0,var0,m1,var1);
    decision_clasico(indice_individuo) = ##completar##;% Guardar aqui la decision del test clasico para cada individuo
end

%---- Simulacion del detector de GT

% Agrupacion de los individuos en grupos de K y calculo del estado infectado/no infectado del grupo
estado_individuos_matriz = reshape(estado_individuos,K,N/K); % Reorganizacion de los individuos en una matriz de 
                                                             % K filas y N/K columnas para facilitar la gestion por grupos
estado_grupos     = ones(1,N/K);% Inicializacion de la variable estado_grupos
                               % La variable estado_grupos es un vector de 1 fila y N/K columnas
                               % con una posicion para el estado de cada grupo                                                           
for indice_grupo=1:N/K
    individuos_en_el_grupo = estado_individuos_matriz(:,indice_grupo);% Pone en un vector los individuos del grupo "indice_grupo"-esimo
 
    estado_grupos (1,indice_grupo) = ##completar##; % Guardar aqui el estado del grupo analizado.
                                                    % El estado de este grupo es infectado si hay algun individuo del grupo que lo esta
end

% Simulacion de las realizaciones del primer test basico
decision_primertest = ones(1,N/K);% Inicializacion de la variable decision_primertest
                                  % La variable decision_primertest es un vector de 1 fila y N/K columnas
                                  % con una posicion para el la decision tomada sobre cada grupo en el primer test
for indice_grupo=1:N/K
    [y] = realizacion_funcion_test (estado_grupos(indice_grupo),m0,var0,m1,var1); % Genera un test basico para cada grupo
    decision_primertest(indice_grupo) = ##completar##; % Guardar aqui la decision del primer test basico
end

% Decisiones y realizacion de los test individuales si es necesario
decision_GT_matriz = ones(K,N/K);  % Inicializacion de la variable decision_GT_matriz 
                                   % Esta variable guarda las decisiones tomadas por el
                                   % detector GT con la misma organizacion de los individuos que 
                                   % el vector estado_individuos_matriz: una matriz de K filas por N/K columnas
                                   % El elemento (i,j) guarda la decision tomada sobre el i-esimo individuo
                                   % del grupo k-esimo

for indice_grupo = 1:N/K
    if decision_primertest(indice_grupo)==0
        decision_GT_matriz(:,indice)=##completar##;
    else
        for indice_individuo_en_grupo=1:K
            [y] =realizacion_funcion_test(##completar##)
            decision_GT_matriz (indice_individuo_en_grupo,indice_grupo)=##completar##;
        end
    end
end

% Reorganizacion de las decisiones en un vector de 1xN
% (las mismas dimensiones que el vector estado_individuos)
decision_GT =reshape(decision_GT_matriz,1,N);
                                     
num_tests_GT_por_individuo = ##completar## % Modificar el software para que calcule el numero promedio  
                                           % de tests realizados por individuo en el detector GT 
                                           % y guarde elresultado aqui

% Evalua P_FA i P_D del detector clasico y el detector GT con los resultados
% de la simulacion por MonteCarlo
P_FA_Clasico_MC = ##completar## % Estimacion de la Prob. Falsa Alarma del detector Clasico
P_FA_GT_MC      = ##completar## % Estimacion de la Prob. Falsa Alarma del detector GT
P_D_Clasico_MC  = ##completar## % Estimacion de la Prob. de Deteccion del detector Clasico
P_D_GT_MC       = ##completar## % Estimacion de la Prob. de Deteccion del detector GT

% A�ade los valores estimados sobre la grafica teorica para comprovar si estan proximos
figure(1); hold on; plot(P_FA_Clasico_MC,P_D_Clasico_MC,'x');
figure(1); hold on; plot(P_FA_GT_MC     ,P_D_GT_MC     ,'o');
figure(2); hold on; plot(num_tests_GT_por_individuo ,P_D_GT_MC     ,'o');


%% ----------- Apartado 4.4: Generacion de una realizacion de la funcion de test

function [y] = realizacion_funcion_test (estado,m0,var0,m1,var1)
% Generacion de una muestra de la funcion de test
% Parametros: 
%    estado : hipotesis con la que se genera la muestra: estado=0 para H0,estado=1 para H1
%    m0,var0: media y varianza de la funcion de test con la hipotesis H0
%    m1,var1: media y varianza de la funcion de test con la hipotesis H1
%    y      : realizacion de la funcion de test con la estadistica deseada

##completar##

end %End function

        


    