CREATE DATABASE api_monitor
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE api_monitor;

CREATE TABLE apis (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      nome VARCHAR(100) NOT NULL,
                      url VARCHAR(500) NOT NULL,
                      ativo BOOLEAN NOT NULL DEFAULT TRUE,
                      criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE monitoramentos (
                                id BIGINT AUTO_INCREMENT PRIMARY KEY,
                                api_id INT NOT NULL,
                                status VARCHAR(30) NOT NULL,
                                codigo_http INT NULL,
                                tempo_resposta_ms DECIMAL(10, 2) NULL,
                                erro TEXT NULL,
                                verificado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                                CONSTRAINT fk_monitoramentos_apis
                                    FOREIGN KEY (api_id)
                                        REFERENCES apis(id)
);

INSERT INTO apis (nome, url)
VALUES
    ('GitHub', 'https://api.github.com'),
    ('ViaCEP', 'https://viacep.com.br/ws/01001000/json/'),
    ('JSONPlaceholder', 'https://jsonplaceholder.typicode.com/posts/1');

SELECT * FROM apis;


SELECT
    a.nome,
    m.status,
    m.codigo_http,
    m.tempo_resposta_ms,
    m.verificado_em
FROM monitoramentos AS m
         INNER JOIN apis AS a
                    ON a.id = m.api_id
ORDER BY m.verificado_em DESC;