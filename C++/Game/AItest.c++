// CustomAIController.h_________________________________________________

#pragma once

#include "CoreMinimal.h"
#include "AIController.h"
#include "CustomAIController.generated.h"

UCLASS()
class YOURPROJECT_API ACustomAIController : public AAIController
{
    GENERATED_BODY()

public:
    // Constructor
    ACustomAIController();

    virtual void OnPossess(APawn* InPawn) override;
};

// CustomAIController.cpp_______________________________________

#include "CustomAIController.h"

ACustomAIController::ACustomAIController()
{
}

void ACustomAIController::OnPossess(APawn* InPawn)
{
    Super::OnPossess(InPawn);

    // Implement behavior tree setup and blackboard usage here.
}

// Inside CustomAIController.cpp_________________________________________

#include "CustomAIController.h"
#include "BehaviorTree/BehaviorTreeComponent.h"
#include "BehaviorTree/BlackboardComponent.h"

ACustomAIController::ACustomAIController()
{
    // Create the behavior tree component and blackboard component.
    BehaviorTreeComponent = CreateDefaultSubobject<UBehaviorTreeComponent>(TEXT("BehaviorTreeComponent"));
    BlackboardComponent = CreateDefaultSubobject<UBlackboardComponent>(TEXT("BlackboardComponent"));
}

void ACustomAIController::OnPossess(APawn* InPawn)
{
    Super::OnPossess(InPawn);

    if (BehaviorTree)
    {
        // Initialize the blackboard with the pawn and any other necessary variables.
        BlackboardComponent->InitializeBlackboard(*BehaviorTree->BlackboardAsset);

        // Run the behavior tree.
        BehaviorTreeComponent->StartTree(*BehaviorTree);
    }
}
