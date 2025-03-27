# DirectX no Projeto: Suporte a Ray Tracing e IA

## 1. Por que DirectX (especificamente DirectX 12 Ultimate)?

- **Padrão da indústria para Windows**: A maioria dos jogos modernos usa DX12, especialmente com Ray Tracing e DLSS.
  
- **Suporte nativo a tecnologias avançadas**:
    - **DirectX Raytracing (DXR)**: API oficial para Ray Tracing em jogos.
    - **DLSS 3/XeSS**: Integração direta via NVIDIA/Intel SDKs.
    - **Mesh Shaders e Sampler Feedback**: Melhor otimização de recursos.

## 2. Vantagens (RTX 3060 vs. RTX 4060)

| Recurso                         | Impacto no Desempenho                                                   |
|----------------------------------|-------------------------------------------------------------------------|
| **DirectX 12 Ultimate (DXR)**    | Habilita Ray Tracing em jogos como *Cyberpunk 2077* e *Alan Wake 2*.    |
| **DLSS 3 (Frame Generation)**    | Exclusivo para DX12 em GPUs RTX 40xx (ganhos de até 2x FPS).            |
| **Melhor Otimização para NVIDIA**| Drivers e ferramentas (NVIDIA Nsight) são mais refinados para DX12.     |

## 3. Limitações

- **Só funciona no Windows**: Não é multiplataforma como Vulkan.
- **Overhead de CPU maior que Vulkan**: Pode limitar desempenho em CPUs muito antigas.

- **Testes com Ray Tracing**:
    - Ativar DXR em *Cyberpunk 2077* e *Hogwarts Legacy* para comparar RTX 3060 vs. 4060.
  
- **Benchmark DLSS 3**:
    - Medir FPS com DLSS Quality/Performance em DX12 (já que FSR funciona em ambas APIs).
  
- **Análise de Estabilidade**:
    - Verificar se DX12 causa stuttering ou melhorias em 1% Low FPS.

**Observação**: Se o projeto fosse incluir Linux/mobile, Vulkan seria necessário, mas como o foco é Windows + NVIDIA, DX12 é a melhor escolha.