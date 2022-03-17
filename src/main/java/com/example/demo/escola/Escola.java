package com.example.demo.escola;

import javax.persistence.*;

//@Entity
//@Table
public class Escola {

    //@Id
    //@GeneratedValue(strategy = GenerationType.SEQUENCE)
    int id;

    String nome;
    Endereco endereco;

    public Escola() {
    }

    public Escola(String nome, Endereco endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }

    public Escola(int id, String nome, Endereco endereco) {
        this.id = id;
        this.nome = nome;
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return "Escola{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", endereco=" + endereco +
                '}';
    }
}
