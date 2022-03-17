package com.example.demo.aluno;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "api/v1")
public class AlunoController {

    @Autowired
    private AlunoRepository alunoRepository;

    @GetMapping("/alunos")
    public List<Aluno> getAll(){
        return alunoRepository.findAll();
    }

    @GetMapping("/alunos/{id}")
    public Aluno getById(@PathVariable Integer id){
        return alunoRepository.getById(id);
    }

    @PostMapping("/alunos")
    public Aluno create(@RequestBody Aluno aluno){
        return alunoRepository.save(aluno);
    }

    @DeleteMapping("/alunos/{id}")
    public void remove(@PathVariable Integer id){
        alunoRepository.deleteById(id);
    }
}
