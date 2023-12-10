# Game Core Structure


## Utility

```mermaid
classDiagram
    class Position {
        -int _x
        -int _y

        +get_x() int
        +set_x() int
        +get_y() int
        +set_y() int
    }
```

## Agent

```mermaid
classDiagram

    class Face {
        UP
        DOWN
        LEFT
        RIGHT
    }
    <<Enumeration>> Face

    class Agent {
        -Position postion;
        -Face current_face
        
        +get_position() Position
        +set_position() Position
        +get_face() Face

        +move(Position original_postion, Position desination_postion) None
        +move_to(Position position) None
    }

    class BasePacMan {

    }
    class BaseGhost {
        +generate_move(List~Position~ pacman_positions)*
    }

    Agent <|-- BasePacMan
    Agent <|-- BaseGhost

```

## PacMan

```mermaid
classDiagram

    class BasePacMan {

    }
    class PacManUser {

    }
    class PacManAI {
        +generate_move(List~Position~ ghost_positions)
    }

    BasePacMan <|-- PacManUser
    BasePacMan <|-- PacManAI
```

## Ghost

```mermaid
classDiagram

    class BaseGhost {
        +generate_move(List~Position~ pacman_positions)*
    }

    class Blinky {
        +generate_move(List~Position~ pacman_positions)
    }
    class Inky {
        +generate_move(List~Position~ pacman_positions)
    }
    class Pinky {
        +generate_move(List~Position~ pacman_positions)
    }
    class Clyde {
        +generate_move(List~Position~ pacman_positions)
    }
    
    BaseGhost <|-- Blinky
    BaseGhost <|-- Inky
    BaseGhost <|-- Pinky
    BaseGhost <|-- Clyde

```

## Field

```mermaid
classDiagram
    
    
    class Square {
        EMPTY
        DOT
        BIGDOT
        WALL
    }
    class Fruit {

    }
    <<Enumeration>> Square
    
    class Event {
        NORMAL
        REVERSE
    }
    <<Enumeration>> Event

    class Field {

        -List~List~Square~~ field
        -Event current_event
        -int live_count
        
        -PacManUser pacman_user
        -PacManAI pacman_ai
        -Blinky blinky
        -Inky inky
        -Pinky pinky
        -Clyde clyde

        -List~Fruit~ fruits
        
        -check_collision() bool
        +update() None
        +isGameOver() bool
    }

```
