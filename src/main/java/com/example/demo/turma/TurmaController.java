package com.example.demo.turma;

import com.example.demo.aluno.Aluno;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "api/v1")
public class TurmaController {

    @Autowired
    private TurmaRepository turmaRepository;

    @GetMapping("/turmas")
    public List<Turma> getAll(){
        return turmaRepository.findAll();
    }

    @GetMapping("/turmas/{id}")
    public Turma getById(@PathVariable Integer id){
        return turmaRepository.getById(id);
    }

    @PostMapping("/turmas")
    public Turma create(@RequestBody Turma turma){
        return turmaRepository.save(turma);
    }

    @DeleteMapping("/turmas/{id}")
    public void remove(@PathVariable Integer id){
        turmaRepository.deleteById(id);
    }

}
